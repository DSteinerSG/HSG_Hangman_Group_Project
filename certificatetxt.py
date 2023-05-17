# to be able to open the newly created txt document in a seperate window the following extensions must be imported
import os
import subprocess

# here we define the function for actually opening the certificate
def open_certificate(certificate):
    # we need to differentiate the different commands for each operating system
    # to achieve this, we use if statements
    if os.name == 'nt':  # Windows
        with open('certificate.txt', 'w') as file:
            file.write(certificate)
        subprocess.run(['start', 'certificate.txt'], shell=True)
    elif os.name == 'posix':  # macOS or Linux
        with open('certificate.txt', 'w') as file:
            file.write(certificate)
        subprocess.run(['open', 'certificate.txt'])
    # if neither the Windows nor the macOS/Linux command is applicable we need to print an error message
    else:
        print("Unsupported operating system: cannot print the certificate.")

# here we create the template for the certificate we want to generate
# with curly brackets we can pass in variables which we want to to be included in the certificate
certificate_template = """

_____________________________________________________________________________________________________

**************************************| Congratulations |********************************************

_____________________________________________________________________________________________________


You, {name}, have successfully completed our hangman game on difficulty {difficulty}!

We hope you will play again soon!

_____________________________________________________________________________________________________

"""

# Variable values for the certificate (we need to adjust these when putting the code together)
name = "John Doe"
difficulty = "medium"

# Generate the certificate by passing in the variables
certificate = certificate_template.format(name=name, difficulty=difficulty)

# Print the certificate by using the function defined earlier
open_certificate(certificate)
