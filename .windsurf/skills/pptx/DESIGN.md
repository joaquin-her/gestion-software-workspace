---
name: Productivity-Focused Scheduling System
colors:
  surface: '#faf8ff'
  surface-dim: '#d9d9e5'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3fe'
  surface-container: '#ededf9'
  surface-container-high: '#e7e7f3'
  surface-container-highest: '#e1e2ed'
  on-surface: '#191b23'
  on-surface-variant: '#434655'
  inverse-surface: '#2e3039'
  inverse-on-surface: '#f0f0fb'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#943700'
  on-tertiary: '#ffffff'
  tertiary-container: '#bc4800'
  on-tertiary-container: '#ffede6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#7d2d00'
  background: '#faf8ff'
  on-background: '#191b23'
  surface-variant: '#e1e2ed'
typography:
  h1:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  grid-margin: 24px
  grid-gutter: 16px
---

## Brand & Style

This design system is engineered for high-utility productivity environments where multi-role coordination is the primary task. The brand personality is rooted in **Modern Corporate** aesthetics—prioritizing clarity, reliability, and emotional calm. By utilizing generous whitespace and a disciplined color application, the UI minimizes cognitive load for users managing complex schedules.

The visual style leverages a "Clean Slate" philosophy: backgrounds are intentionally quiet to allow active scheduling data to take precedence. The target audience includes administrative professionals, service providers, and end-clients, requiring a design that scales from high-density data views to simplified booking flows.

## Colors

The palette is anchored by a vibrant, professional Primary Blue (#2563EB), which acts as the primary driver for interaction and focus. Neutral tones are meticulously layered: **White (#FFFFFF)** is reserved for the primary content "stage" or cards, while **Light Gray (#F9FAFB)** defines the workspace background to create a subtle containment effect.

Functional accents (Success and Error) are applied with low saturation to maintain the "calm" atmosphere, ensuring that alerts do not cause unnecessary alarm while remaining clearly legible. Text hierarchy is maintained through a range of slate grays to ensure high contrast without the harshness of pure black.

## Typography

This design system utilizes **Inter** as the sole typeface to leverage its exceptional legibility in data-heavy SaaS interfaces. The typographic scale is optimized for information density. 

Headlines use tighter letter-spacing and heavier weights to provide clear section anchoring. Body text prioritizes a comfortable line height (1.5x to 1.6x) to facilitate scanning of long lists or appointment details. Labels utilize medium and semi-bold weights at smaller scales to differentiate metadata from primary content without relying on color alone.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid Grid**. Content is housed within a 12-column system with a maximum width for desktop monitors to prevent "line-length fatigue" in dashboard views. 

The spacing rhythm is built on a 4px base unit. 
- **16px (md)** is the standard padding for cards and input containers.
- **24px (lg)** is used for section gaps and page margins.
- A clear vertical hierarchy is established by using consistent `xl` spacing between major layout blocks (e.g., the transition from the header to the main scheduling grid).

## Elevation & Depth

Depth is conveyed through **Tonal Layering** supplemented by **Ambient Shadows**. 

1.  **Level 0 (Floor):** The application background uses the light gray neutral.
2.  **Level 1 (Surface):** Primary content containers (Calendars, Lists, Forms) are white with a subtle 1px border (#E5E7EB) and a very soft, diffused shadow (0px 2px 4px rgba(0,0,0,0.05)).
3.  **Level 2 (Interaction):** Hover states on cards or interactive elements increase the shadow spread slightly.
4.  **Level 3 (Overlay):** Modals and dropdowns use a more pronounced shadow (0px 10px 15px rgba(0,0,0,0.1)) to visually lift them above the functional workspace.

Shadows should never be "black"; they are slightly tinted with the primary blue to maintain the professional, clean aesthetic.

## Shapes

The design system employs a **Rounded (Level 2)** shape language to soften the "industrial" feel of a scheduling tool and make it more approachable. 

- Standard components (Buttons, Inputs, Chips) utilize a **0.5rem (8px)** corner radius.
- Large containers (Cards, Modals) use **1rem (16px)** to emphasize their structural importance. 
- This consistency in radius helps unify different roles’ perspectives, from a high-level admin dashboard to a client-facing booking widget.

## Components

### Buttons
Buttons are the primary action drivers. The **Primary Button** is a solid fill of #2563EB with white text. **Secondary Buttons** use a light gray ghost style or a subtle outline to avoid competing for attention.

### Inputs & Selects
Field borders are light gray (#D1D5DB) and transition to the Primary Blue on focus. Labels are consistently placed above the field in `label-md` style.

### Chips & Status Indicators
Used for appointment statuses (e.g., "Pending," "Confirmed"). These use a "Soft Fill" approach: a very light version of the status color (e.g., light green background) with a high-contrast dark text of the same hue.

### Cards
Cards are the backbone of the scheduling view. Each card must have a clear title and a distinct "Action Area" at the bottom for quick modifications.

### Navigation
The sidebar navigation uses a subtle tonal shift from the main background. Active states are indicated by a vertical 4px bar of Primary Blue on the leading edge and a subtle weight increase in the text.

### Scheduling Grid
The central component requires high-density styling. Time slots should be demarcated by 1px light gray lines, and "occupied" blocks should use the primary color with 10% opacity to remain legible without being overwhelming.