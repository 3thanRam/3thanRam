from jinja2 import Environment, FileSystemLoader
import datetime

def main():
    # Get the current timestamp in UTC and format it
    #updated_at = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Articles data
    list_data = [
        {"title": "0", "elements": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
    ]


    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('README.md.j2')

    # Render and merge templates
    rendered_readme = template.render(list=list_data)

    # Save to README.md
    with open("README.md", "w") as f:
        f.write(rendered_readme)


if __name__ == "__main__":
    main()