import requests
from bs4 import BeautifulSoup

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_emails, subject, body):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipient_emails)  # Join the list of recipients
    message['Subject'] = subject

    # Add the body text to the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted TLS connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_emails, message.as_string())
        print(f"Email sent successfully to {', '.join(recipient_emails)}")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

    finally:
        server.quit()

try:
    cookies = {
        'rbzsessionid': '8137a25ccd816c0b4080d0a45e87f569',
        'device_id': '756c102b-3967-4025-9121-c09af1dc8a3e',
        'intercom-id-f9d90yaf': '97767af5-ae55-4c8f-b58b-94293a7fe8d5',
        'intercom-session-f9d90yaf': '',
        'intercom-device-id-f9d90yaf': 'bb9241e5-57d3-4100-8478-e7badc0974aa',
        'rbzid': 'uyF3NU77FrwZ0srQLiQZTR7LCv6mvMesNeld1Ynh1xGdsnguBBhr2uENMm6v2Mqf288YewPIPw27aPnipm05W2obHtk1r9qDkSJacnR4sbJ+Mbs+4r3QrAP6AJh6JxZ2iLZ7JGpilxRGAaDnBXPvMWDtWzaTxKfE0a8YV4yZYMPsqLzzpLYhvNaFZNYQ2pVX9WxTR03z5/DGgSRgc01TXMauWD5qXDtoMr9pYDcCTtI=',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,und;q=0.7,hu;q=0.6',
        'cache-control': 'no-cache',
        # 'cookie': 'rbzsessionid=8137a25ccd816c0b4080d0a45e87f569; device_id=756c102b-3967-4025-9121-c09af1dc8a3e; intercom-id-f9d90yaf=97767af5-ae55-4c8f-b58b-94293a7fe8d5; intercom-session-f9d90yaf=; intercom-device-id-f9d90yaf=bb9241e5-57d3-4100-8478-e7badc0974aa; rbzid=uyF3NU77FrwZ0srQLiQZTR7LCv6mvMesNeld1Ynh1xGdsnguBBhr2uENMm6v2Mqf288YewPIPw27aPnipm05W2obHtk1r9qDkSJacnR4sbJ+Mbs+4r3QrAP6AJh6JxZ2iLZ7JGpilxRGAaDnBXPvMWDtWzaTxKfE0a8YV4yZYMPsqLzzpLYhvNaFZNYQ2pVX9WxTR03z5/DGgSRgc01TXMauWD5qXDtoMr9pYDcCTtI=',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.ticketswap.com/event/dnb-allstars-halloween-360-bristol/24947ebf-2593-478b-b7a6-b165c0bcc996',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    url = 'https://www.ticketswap.com/event/dnb-allstars-halloween-360-bristol/24947ebf-2593-478b-b7a6-b165c0bcc996'

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )
    
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all h2 tags
    h2_tags = soup.find_all('h2')

    # Iterate over each h2 tag to find the one with the text "Tickets"
    for h2 in h2_tags:
        if h2.text.strip() == "Tickets":
            # print("Found 'Tickets' section:", h2)
            available_tickets = int(h2.find_next('span').text.strip().replace('<!-- -->', '').split(' • ')[0].replace(" available", ""))
            print(available_tickets)
            if available_tickets > 0:
                sender_email = 'thekiadoe@gmail.com'
                sender_password = 'kbmx nmnx ifha vnyk'  # Or app-specific password if 2FA is enabled
                recipient_emails = ['thekiadoe@gmail.com','pippa1996@hotmail.com']  # List of recipients
                subject = '!!!TICKETS AVAILABLE!!!'
                body = f'<a href="{url}">{url}<a/>'
                send_email(sender_email, sender_password, recipient_emails, subject, body)
                exit()
            
except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching the page: {str(e)}")
