import smtplib
import email.message

def enviar_email_user(email_user):  
    corpo_email = f"""
                <h2>Olá <b>{email_user}</b>!</h2>
                <p style='font-size:12pt'>
                    Essa é uma mensagem diretamente enviada do desenvolvedor <br>
                    Pedro Lucas Da Silva Rosa.
                </p> <br>
                <br>

                <p>
                    Fico extremamente agradecido que tenha visitado minha landing page! <br>
                    Caso tenha vindo pelo curso oferecido, peço desculpas por isso, <br>
                    pois o conteúdo oferecido na landing page não é verídico.
                </p> <br>
                <br>

                <p>
                    Caso tenha interesse em meus serviços entre em contato! <br>
                    Email: pedrolucass1106@gmail.com <br>
                    LinkedIn: <a href='https://www.linkedin.com/in/pedro-lucas-da-silva-rosa-94211a334/'>Meu Perfil LinkedIn</a> <br>
                    Workana: <a href='https://www.workana.com/freelancer/c01008fa8d4ef7b55d4a5384d9524715'>Meu Perfil Workana</a> <br>
                </p> <br>
                <br>

                <p>
                    Deixarei aqui o link para o meu portfólio também: <br>
                    <a href='https://pedrionsx.github.io/pedrolucas.github.io/'>Portfólio</a>
                </p>
                   """

    msg = email.message.Message()
    msg['Subject'] = "Landing Page Desenvolvida por Pedro Lucas"
    msg['From'] = 'pedrolucass1106@gmail.com'
    msg['To'] = email_user
    password = 'rjiqnwcpzwxcdcvr' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))