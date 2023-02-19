import { MARK } from "../constants.ts";

export const updateReadme = async (user: string) => {
  const README_FILE_PATH = "./README.md";

  const readme = await Deno.readTextFile(README_FILE_PATH);
  const markerPattern = new RegExp(`(${MARK.START})[\\s\\S]*(${MARK.END})`);
  if (!markerPattern.test(readme)) {
    throw new Error("Error: MARKER is not exists in README.md");
  }

  const markup = `
<a href="https://leetcode.com/${user}/" target="_blank">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/problems_dark.png" width="500">
  <img alt="" src="./images/problems.png" width="500">
</picture>
</a>
<a href="https://leetcode.com/${user}/" target="_blank">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/streak_dark.png">
  <img alt="" src="./images/streak.png">
</picture>
</a>
  \nLast Updated on ${new Date().toLocaleString()}
  `

  const newReadme = readme.replace(markerPattern, `$1\n${markup}\n$2`);

  await Deno.writeTextFile(README_FILE_PATH, newReadme);
};
