import time

from whatsapp import (
    read_chat,
    get_last_message,
    send_message
)

from ai import generate_reply


def start_bot():

    print("=" * 50)
    print(" WhatsApp AI Agent")
    print("=" * 50)

    print("\nReading current chat...")

    current_chat = read_chat()

    if not current_chat:

        print("Could not read WhatsApp chat.")

        return

    previous_chat = current_chat

    current_last_message = get_last_message(
        current_chat
    )

    print("\nCurrent last message:")
    print(current_last_message)

    # ---------------------------------
    # IMPORTANT
    # Remember the message sent by bot
    # ---------------------------------

    bot_sent_message = None

    print("\nAgent started.")
    print("Waiting for new message...\n")


    while True:

        try:

            time.sleep(5)

            current_chat = read_chat()

            if not current_chat:
                continue


            # ==================================
            # CHAT DID NOT CHANGE
            # ==================================

            if current_chat == previous_chat:

                continue


            # ==================================
            # GET LAST MESSAGE
            # ==================================

            last_message = get_last_message(
                current_chat
            )

            print("\n" + "=" * 50)
            print("CHAT CHANGED")
            print("=" * 50)

            print("\nLast message:")
            print(last_message)


            # ==================================
            # IGNORE OUR OWN MESSAGE
            # ==================================

            if (
                bot_sent_message
                and
                last_message.strip()
                == bot_sent_message.strip()
            ):

                print(
                    "\n🤖 This is my own message."
                )

                print(
                    "Ignoring it and waiting..."
                )

                previous_chat = current_chat

                continue


            # ==================================
            # NEW REAL MESSAGE
            # ==================================

            print("\n📩 NEW MESSAGE DETECTED")

            print("IMPORTANT: sender detection is not enabled yet.")

            # ==================================
            # GROQ
            # ==================================

            print("\n🧠 Asking Groq...")

            reply = generate_reply(
                current_chat
            )

            if not reply:

                print(
                    "❌ Empty AI response."
                )

                previous_chat = current_chat

                continue


            print("\n🤖 AI Reply:")
            print(reply)


            # ==================================
            # SAVE BEFORE SENDING
            # ==================================

            bot_sent_message = reply.strip()


            # ==================================
            # SEND
            # ==================================

            send_message(reply)


            print(
                "\n✅ Reply sent."
            )


            # ==================================
            # UPDATE CHAT
            # ==================================

            previous_chat = current_chat


        except KeyboardInterrupt:

            print("\n\nBot stopped.")

            break


        except Exception as e:

            print(
                "\n❌ ERROR:"
            )

            print(e)

            time.sleep(3)
