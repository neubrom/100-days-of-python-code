
import smtplib
my_email = "42robro@gmail.com"
password ="O4_Romaschka_009"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="poltoratsky@gmail.com",
        msg="Subject:Hello\n\n This is thr body of my email")
