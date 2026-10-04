import reflex as rx

from app.states.navigation_state import NavigationState


def navigation_links() -> rx.Component:
    return rx.fragment(
        rx.el.a(
            "خانه",
            href="https://farzaneganehooshmand.com/",
            aria_current="page",
            class_name="rounded-lg px-3 py-3 text-[#4eacd9] transition-colors hover:bg-[#edf7fc] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
        ),
        rx.el.a(
            "مقالات",
            href="https://farzaneganehooshmand.com/blog/",
            class_name="rounded-lg px-3 py-3 text-[#102d4b] transition-colors hover:bg-[#edf7fc] hover:text-[#4eacd9] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
        ),
        rx.el.a(
            "محصولات",
            href="https://farzaneganehooshmand.com/shop/",
            class_name="rounded-lg px-3 py-3 text-[#102d4b] transition-colors hover:bg-[#edf7fc] hover:text-[#4eacd9] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
        ),
        rx.el.a(
            "تماس با ما",
            href="https://farzaneganehooshmand.com/contact-us/",
            class_name="rounded-lg px-3 py-3 text-[#102d4b] transition-colors hover:bg-[#edf7fc] hover:text-[#4eacd9] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
        ),
        rx.el.a(
            "درباره ما",
            href="https://farzaneganehooshmand.com/about-us/",
            class_name="rounded-lg px-3 py-3 text-[#102d4b] transition-colors hover:bg-[#edf7fc] hover:text-[#4eacd9] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
        ),
    )


def account_link() -> rx.Component:
    return rx.el.a(
        rx.icon("user-round", class_name="h-4 w-4"),
        "حساب کاربری",
        href="https://farzaneganehooshmand.com/my-account/",
        class_name="flex w-fit items-center justify-center gap-2 rounded-xl border border-[#d7e8f1] bg-white px-4 py-3 text-sm font-medium text-[#102d4b] transition-colors hover:border-[#4eacd9] hover:bg-[#edf7fc] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.img(
                    src="https://farzaneganehooshmand.com/wp-content/uploads/2026/07/farzaneganehooshmand-2026-logo-300x124.png",
                    alt="فرزانگان هوشمند، مرکز مشاوره و روانشناسی",
                    width=300,
                    height=124,
                    class_name="h-auto w-36 object-contain sm:w-44",
                ),
                href="https://farzaneganehooshmand.com/",
                aria_label="صفحه اصلی فرزانگان هوشمند",
                class_name="shrink-0 rounded-lg focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
            ),
            rx.el.nav(
                navigation_links(),
                aria_label="منوی اصلی",
                class_name="hidden items-center gap-2 text-sm font-medium lg:flex",
            ),
            rx.el.div(account_link(), class_name="hidden lg:block"),
            rx.el.button(
                rx.cond(
                    NavigationState.menu_open,
                    rx.icon("x", class_name="h-6 w-6"),
                    rx.icon("menu", class_name="h-6 w-6"),
                ),
                on_click=NavigationState.toggle_menu,
                type="button",
                aria_label=rx.cond(
                    NavigationState.menu_open, "بستن منو", "باز کردن منو"
                ),
                aria_expanded=NavigationState.menu_open,
                aria_controls="mobile-navigation",
                class_name="flex h-11 w-11 items-center justify-center rounded-xl border border-[#d7e8f1] bg-[#f3faff] text-[#102d4b] hover:bg-[#e3f3fc] focus-visible:outline-2 focus-visible:outline-[#4eacd9] lg:hidden",
            ),
            class_name="mx-auto flex w-full max-w-7xl items-center justify-between gap-5 px-5 py-5 sm:px-8 lg:px-10",
        ),
        rx.cond(
            NavigationState.menu_open,
            rx.el.nav(
                navigation_links(),
                rx.el.div(
                    account_link(),
                    class_name="border-t border-[#e2edf3] px-3 pt-4",
                ),
                id="mobile-navigation",
                aria_label="منوی موبایل",
                class_name="flex flex-col gap-1 border-t border-[#e2edf3] bg-white px-5 pb-5 pt-3 text-sm font-medium lg:hidden",
            ),
        ),
        class_name="relative z-20 w-full border-b border-[#e5eff5] bg-white",
    )
