import yagmail



def sendEmail(recipients, subject, content):
    yag = yagmail.SMTP("monitorbroodingrearing@gmail.com", "nlxq wgth phof qjqf")

    yag.send(
        to=recipients,
        subject = subject,
        contents = content
    )
    print("Email Sent Successfully")
