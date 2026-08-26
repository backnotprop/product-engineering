/**
 * OG card: the kit's brand card. Dark linear ground (#1D1F24 → #121316 in
 * DESIGN.md), Geist 600 for the title, Geist Mono for the description. No
 * accent, no border, no mark — the card is type on a quiet gradient.
 */

import type { OGImageOptions } from "astro-og-canvas";

export const ogCardConfig = {
  bgGradient: [
    [29, 31, 36],
    [18, 19, 22],
  ],
  padding: 96,
  fonts: ["./public/fonts/Geist-SemiBold.ttf", "./public/fonts/GeistMono-Regular.ttf"],
  font: {
    title: {
      color: [245, 245, 244],
      size: 64,
      weight: "SemiBold",
      families: ["Geist"],
      lineHeight: 1.1,
    },
    description: {
      color: [139, 141, 148],
      size: 28,
      weight: "Normal",
      families: ["Geist Mono"],
      lineHeight: 1.4,
    },
  },
  format: "PNG",
} satisfies Partial<OGImageOptions>;
