import os, uuid, asyncio, logging

import uvicorn

from google.adk.memory import InMemoryMemoryService
from google.adk.runners import Runner

from google.adk.sessions import InMemorySessionService, Session

from google.genai import types

from Engine.agent import root_agent


from dotenv import load_dotenv

load_dotenv()

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    Update,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    CallbackContext,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Your bot token (get it from @BotFather)
TOKEN = os.environ.get("MEDPALBOT_TOKEN")

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()


APP_NAME = "MedPalAgent"
USER_ID = str(uuid.uuid4())
SESSION_ID = str(uuid.uuid4())  # Using a fixed ID for simplicity
SESSION = None


async def initialize_session():
    SESSION = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID)
    SESSION_ID = SESSION.id
    print(f"Session:  {SESSION}")
    # await memory_service.add_session_to_memory(session=SESSION)
    return SESSION, SESSION_ID


SESSION, SESSION_ID = asyncio.run(initialize_session())
LOCATION, BUTTONS, QUERY = range(3)

runner = Runner(
    agent=root_agent,  # The agent we want to run
    app_name=APP_NAME,  # Associates runs with our app
    session_service=session_service,  # Uses our session manager
)


async def call_agent(runner, user_id, session_id, query):
    """Sends a query to the agent and prints the final response."""
    print(f"\n>>> User Query: {query}")

    root_agent.run_async

    # Prepare the user's message in ADK format
    content = types.Content(role="user", parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response."  # Default

    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                # Assuming text response in the first part
                final_response_text = event.content.parts[0].text
            elif (
                event.actions and event.actions.escalate
            ):  # Handle potential errors/escalations
                final_response_text = (
                    f"Agent escalated: {event.error_message or 'No specific message.'}"
                )
            # Add more checks here if needed (e.g., specific error codes)
            break  # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")
    print(f"Response:  {final_response_text}")
    return final_response_text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send a message with main menu when the command /start is issued."""

    location_button = KeyboardButton(text="Share Location", request_location=True)

    keyboard = ReplyKeyboardMarkup(
        [[location_button]], resize_keyboard=True, one_time_keyboard=True
    )

    await update.message.reply_text(
        "Hi! I am MedPal Bot, your personal expert in healthcare assistant bot. I can help you find nearby pharmacies, health facilities, emergency services, and health professionals based on your location.\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "Please share your location with me to get started.",
        reply_markup=keyboard,
    )

    return LOCATION


async def handle_location(update: Update, context: CallbackContext) -> int:
    location = update.message.location
    user = update.message.from_user
    logger.info(
        "Location of %s: %f / %f",
        user.first_name,
        location.latitude,
        location.longitude,
    )
    context.user_data["location"] = location
    context.user_data["latitude"] = location.latitude
    context.user_data["longitude"] = location.longitude

    latitude = location.latitude
    longitude = location.longitude

    await update.message.reply_text(
        f"Location received!\nLatitude: {latitude}\nLongitude: {longitude}"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "Find Pharmacies Near You 💊", callback_data="pharmaceuticals"
            )
        ],
        [
            InlineKeyboardButton(
                "Find Health Facilities Near You 🏥", callback_data="health_facilities"
            )
        ],
        [
            InlineKeyboardButton(
                "Get In Touch with emergency services Providers Near You   🚨",
                callback_data="emergency_services",
            )
        ],
        [
            InlineKeyboardButton(
                "Talk To A health Proffessional Near You 👨‍⚕ ️",
                callback_data="health_professionals",
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Please choose an option:", reply_markup=reply_markup
    )

    return BUTTONS


async def button(update: Update, context) -> int:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()

    print("Button pressed: %s", query.data)
    print("User data: %s", context.user_data)

    response = "No action taken."

    user_location = {
        "latitude": context.user_data.get("latitude"),
        "longitude": context.user_data.get("longitude"),
    }

    if query.data == "pharmaceuticals":
        response = await call_agent(
            runner,
            USER_ID,
            SESSION_ID,
            f"Find pharmacies near this coodinates: {user_location} ",
        )

    elif query.data == "health_facilities":
        response = await call_agent(
            runner,
            USER_ID,
            SESSION_ID,
            f"Find health facilities near this coodinates: {user_location} ",
        )

    elif query.data == "emergency_services":
        response = await call_agent(
            runner,
            USER_ID,
            SESSION_ID,
            f"Find emergency services near this coodinates: {user_location} ",
        )

    elif query.data == "health_professionals":
        response = await call_agent(
            runner,
            USER_ID,
            SESSION_ID,
            f"Find health proffessionals near this coodinates: {user_location} ",
        )

    await query.message.reply_text(response, reply_markup=ReplyKeyboardRemove())

    return BUTTONS


async def query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    response = await call_agent(runner, USER_ID, SESSION_ID, update.message.text)
    print("I have been called......")

    await update.message.reply_text(
        response,
        reply_markup=ReplyKeyboardRemove(),
    )

    return QUERY


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Use /start to test this bot.")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LOCATION: [MessageHandler(filters.LOCATION, handle_location)],
            BUTTONS: [CallbackQueryHandler(button)],
            QUERY: [MessageHandler(filters.TEXT & ~filters.COMMAND, query)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        conversation_timeout=100000000000000000000000000000000000000000,
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
