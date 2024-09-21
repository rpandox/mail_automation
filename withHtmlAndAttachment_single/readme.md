# Email Bulk Sender

This Python script sends personalized HTML emails in bulk using a contact list from an Excel file. It supports attachments and uses the Jinja2 templating engine for dynamic content.

## Features

- Send personalized bulk emails
- HTML content rendering with Jinja2
- File attachments
- Secure email credentials management

## Requirements

- Python 3.x
- Libraries: `smtplib`, `pandas`, `email`, `python-dotenv`, `jinja2`

Install the required libraries:

```bash
pip install pandas python-dotenv jinja2
```

## Setup

1. Create a `credentials.env` file with your email credentials:

   ```
   username=your_email@gmail.com
   password=your_password
   ```

2. Prepare an Excel file (`Bulk.xlsx`) with columns for `Community Name` and `Email`.
3. Create an HTML file (`email_content.html`) for your email content using Jinja2 syntax for placeholders.

## Usage

Run the script:

```bash
python your_script_name.py
```

## License

MIT License

## Contact

For inquiries, contact [This_mail](mailto:rpandox@gmail.com).

```
Let me know if you need any changes!
```
