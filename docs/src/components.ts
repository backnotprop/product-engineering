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
import SkillCards from "./components/pe/SkillCards.astro";

export const components = {
  Aside,
  Card,
  CardGrid,
  PackageManagers,
  Render,
  SkillCards,
  Step,
  Steps,
  TabItem,
  Tabs,
};
