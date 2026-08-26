/**
 * MDX globals registry — components available inside MDX without `import`.
 */

import { Aside } from "./components/ui/aside";
import Render from "./components/Render.astro";
import { Card } from "./components/ui/card";
import { CardGrid } from "./components/ui/card-grid";
import { PackageManagers } from "./components/ui/package-managers";
import { Step, Steps } from "./components/ui/steps";
import { Tabs, TabItem } from "./components/ui/tabs";
import Modes from "./components/pe/Modes.astro";
import Setup from "./components/pe/Setup.astro";
import Provenance from "./components/pe/Provenance.astro";
import SkillLine from "./components/pe/SkillLine.astro";
import SkillCards from "./components/pe/SkillCards.astro";

export const components = {
  Aside,
  Card,
  CardGrid,
  Modes,
  PackageManagers,
  Provenance,
  Render,
  Setup,
  SkillCards,
  SkillLine,
  Step,
  Steps,
  TabItem,
  Tabs,
};
