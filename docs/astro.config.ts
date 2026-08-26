import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import nimbus, { defineConfig as defineNimbusConfig } from "@cloudflare/nimbus-docs";
import { tableScroll } from "@cloudflare/nimbus-docs/markdown";

const nimbusConfig = defineNimbusConfig({
  // Canonical origin: OG image URLs, robots.txt, the sitemap, and /llms.txt links derive from it.
  site: "https://peskills.dev",
  title: "product engineering",
  description: "Six agent skills for product design and engineering.",
  locale: "en",
  github: "https://github.com/backnotprop/product-engineering",
  editPattern: "https://github.com/backnotprop/product-engineering/edit/main/docs/src/content/docs/{path}",
  socialImageAlt: "product engineering",
  sidebar: {
    items: [
      { label: "Start", autogenerate: { directory: "start" } },
      { label: "Skills", autogenerate: { directory: "skills" } },
      { label: "Workflows", autogenerate: { directory: "workflows" } },
      { label: "People", autogenerate: { directory: "people" } },
      { label: "Reference", autogenerate: { directory: "reference" } },
    ],
  },
});

export default defineConfig({
  output: "static",
  vite: {
    plugins: [tailwindcss()],
  },
  prefetch: {
    prefetchAll: true,
    defaultStrategy: "hover",
  },
  integrations: [
    nimbus(nimbusConfig, {
      rules: {
        "nimbus/frontmatter-shape": "error",
        "nimbus/internal-link": "error",
      },
      markdown: {
        hastPlugins: [tableScroll()],
      },
    }),
  ],
});
