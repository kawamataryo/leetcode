import puppeteer from "https://deno.land/x/puppeteer@16.2.0/mod.ts";
import { z } from "https://deno.land/x/zod@v3.20.2/mod.ts";
import { MARK } from "./constants.ts";

const captureStreak = async (user: string) => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.setViewport({
    width: 1200,
    height: 1500
})

  await page.goto(`https://leetcode.com/${user}/`, {
    waitUntil: "networkidle0",
  });

  await page.emulateMediaFeatures([
    { name: "prefers-color-scheme", value: "dark" },
  ]);
  const selector =
    "//span[contains(., 'submissions in the last year')]/parent::div/parent::div/parent::div";
  await page.waitForXPath(selector);
  const element = await page.$x(selector); // declare a variable with an ElementHandle

  await Deno.mkdir("images", {
    'recursive': true
  });

  // capture light mode
  await element[0].screenshot({ path: "images/streak.png" });

  // capture dark mode
  const htmlHandle = await page.$("html");
  await page.evaluate((html) => {
    html.classList.add("dark");
  }, htmlHandle);

  await element[0].screenshot({ path: "images/streak_dark.png" });

  await browser.close();
};

const updateReadme = async () => {
    const README_FILE_PATH = './README.md'

    const readme = await Deno.readTextFile(README_FILE_PATH);
    const markerPattern = new RegExp(`(${MARK.START})[\\s\\S]*(${MARK.END})`)
    if (!markerPattern.test(readme)) {
      throw new Error("Error: MARKER is not exists in README.md")
    }

    const updateTime = `  \nLast Updated on ${new Date().toLocaleString()}`
    readme.replace(markerPattern, `$1\n${updateTime}\n$2`)

    await Deno.writeTextFile(README_FILE_PATH, readme);
}

const main = async () => {
  // capture image
  const user = z.string().parse(Deno.env.get("LEET_CODE_USER_NAME"));
  await captureStreak(user);

  // update README
  await updateReadme()
};

main();
