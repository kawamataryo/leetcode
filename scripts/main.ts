import { z } from "https://deno.land/x/zod@v3.20.2/mod.ts";
import { capturePage } from "./lib/capturePage.ts";
import { updateReadme } from "./lib/updateReadme.ts";


const main = async () => {
  const user = z.string().parse(Deno.env.get("LEET_CODE_USER_NAME"));

  await capturePage(user);
  await updateReadme(user);
};

main();
