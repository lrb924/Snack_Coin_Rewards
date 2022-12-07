# Imports
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

def create_message(customer_info, food_, order_id, order_total, order_tokens):

    wallet = customer_info['wallet']
    first_name = customer_info['first_name']
    last_name = customer_info['last_name']
    name = f"{first_name} {last_name}"
    email = customer_info['email']
    email_split = email.split('@')

    # Create the base text message.
    msg = EmailMessage()
    msg['Subject'] = "SnackCoin Rewards Test Order"
    msg['From'] = Address("SnackCoin Rewards", "snackcoin", "test.com")
    msg['To'] = Address(
        name,
        email_split[0],
        email_split[1]
    )
    msg.set_content(f"""\
    Hello {name}!

    You placed an order: #{order_id}
    
    The total was {order_total}

    This is a test email
    """)

    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.

    msg.add_alternative("""\
        <h1 id="-thanks-for-your-order-">💥 Thanks for your order!</h1>
        <br>
        <h2 id="order-confirmation-br-">Order Confirmation <br></h2>
            <p>Order: #{} <br></p>
            <p>Hi {}, <br></p>
            <p>Your order #{} is completed. <br></p>
            <p>Total: {} ETH <br></p>
            <p>SNAK coins earned: {} 😃 <br></p>
            <p>Eat more, earn more!</p>
        """.format(order_id, first_name, order_id, order_total, order_tokens),
        subtype='html'
    )

    return msg

def send_email(msg):
    # Send the message via local SMTP server.
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)
