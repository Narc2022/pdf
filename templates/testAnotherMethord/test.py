import subprocess

def generate_pdf(input_file, output_file):
    try:
        # Use subprocess to call wkhtmltopdf with the input HTML file and desired output file
        subprocess.run(['wkhtmltopdf', input_file, output_file], check=True)
        print(f'PDF generated successfully at: {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error generating PDF: {e}')

# Example usage
input_file = 'main.html'
output_file = 'output.pdf'

generate_pdf(input_file, output_file)