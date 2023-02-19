import puppeteer from "https://deno.land/x/puppeteer@16.2.0/mod.ts";

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto("https://leetcode.com/kawamataryo/", {
  waitUntil: "networkidle2",
});

await page.emulateMediaFeatures([
  { name: "prefers-color-scheme", value: "dark" },
]);
const selector = "//span[contains(., 'submissions in the last year')]/parent::div/parent::div/parent::div"
await page.waitForXPath(selector);
const element = await page.$x(selector);        // declare a variable with an ElementHandle

// light mode
await element[0].screenshot({ path: "images/streak.png" });

// dark mode
const htmlHandle = await page.$('html')
await page.evaluate((html) => {
  html.classList.add("dark")
}, htmlHandle)

await element[0].screenshot({ path: "images/streak_dark.png" });

await browser.close();
