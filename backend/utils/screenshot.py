from playwright.async_api import Page


async def screenshot(page: Page):
    return await page.screenshot(type="png")