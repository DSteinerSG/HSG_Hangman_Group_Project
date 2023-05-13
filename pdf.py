#import the necessary extensions
#hier habe ich noch Probleme, das scheint auf meinem Mac nicht so zu klappen wie im Beispiel
import jinja2
import pdfkit
from datetime import datetime

#hier können wir die Variablen einfach an die sonst genutzten anpassen
my_name = "Max Mustermann"
number_of_tries = "5"
#save date as a variable
today_date = datetime.today().strftime("%d %b, %Y")

#pass context into the code which is generating the pdf
context = {'my_name': my_name, 'number_of_tries': number_of_tries,'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'basic-template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(Certificate='/usr/local')
output_pdf = 'pdf_generated.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')
