from django import template
from menu_app.models import MenuItem

register = template.Library()


def get_menu_hierarchy(menu_name):
    items = (
        MenuItem.objects.filter(menu__name=menu_name)
        .select_related("parent")
        .order_by("parent_id", "id")
    )
    menu_dict = {}
    for item in items:
        menu_dict.setdefault(item.parent_id, []).append(item)
    return build_menu_tree(menu_dict, None)


def build_menu_tree(menu_dict, parent_id):
    tree = []
    for item in menu_dict.get(parent_id, []):
        item.children = build_menu_tree(menu_dict, item.id)
        tree.append(item)
    return tree


@register.inclusion_tag("menu_app/menu.html")
def draw_menu(menu_name):
    menu = get_menu_hierarchy(menu_name)
    return {"menu": menu}
