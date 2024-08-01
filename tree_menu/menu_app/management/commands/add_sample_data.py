# app/management/commands/add_sample_data.py
from django.core.management.base import BaseCommand
from menu_app.models import Menu, MenuItem


class Command(BaseCommand):
    help = "Add sample menu data"

    def handle(self, *args, **kwargs):
        self.add_sample_data()

    def add_sample_data(self):
        # Clear existing data
        MenuItem.objects.all().delete()
        Menu.objects.all().delete()

        # Create sample menus
        main_menu = Menu.objects.create(name="main_menu")
        footer_menu = Menu.objects.create(name="footer_menu")

        # Create sample menu items for main menu
        home = MenuItem.objects.create(name="Home", url="/home/", menu=main_menu)
        about = MenuItem.objects.create(name="About", url="/about/", menu=main_menu)
        services = MenuItem.objects.create(
            name="Services", url="/services/", menu=main_menu
        )

        # Add sub-items to 'Services'
        web_development = MenuItem.objects.create(
            name="Web Development",
            url="/services/web-development/",
            menu=main_menu,
            parent=services,
        )
        web_design = MenuItem.objects.create(
            name="Web Design",
            url="/services/web-development/web-design/",
            menu=main_menu,
            parent=web_development,
        )
        seo = MenuItem.objects.create(
            name="SEO", url="/services/seo/", menu=main_menu, parent=services
        )
        marketing = MenuItem.objects.create(
            name="Marketing",
            url="/services/marketing/",
            menu=main_menu,
            parent=services,
        )

        # Create sample menu items for footer menu
        contact = MenuItem.objects.create(
            name="Contact", url="/contact/", menu=footer_menu
        )
        privacy_policy = MenuItem.objects.create(
            name="Privacy Policy", url="/privacy-policy/", menu=footer_menu
        )

        self.stdout.write(self.style.SUCCESS("Sample menu data added successfully!"))
