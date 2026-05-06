---
name: PPTX Presentation Design System
colors:
  surface: '#ffffff'
  surface-dim: '#f3f4f6'
  surface-bright: '#ffffff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8fafc'
  surface-container: '#e5e7eb'
  surface-container-high: '#d1d5db'
  surface-container-highest: '#9ca3af'
  on-surface: '#1a1a2e'
  on-surface-variant: '#5a6a7a'
  inverse-surface: '#1a2e4a'
  inverse-on-surface: '#ffffff'
  outline: '#6b7a8d'
  outline-variant: '#b2d8d8'
  surface-tint: '#1a2e4a'
  primary: '#1a2e4a'
  on-primary: '#ffffff'
  primary-container: '#14b0e2'
  on-primary-container: '#ffffff'
  inverse-primary: '#b2d8d8'
  secondary: '#14b0e2'
  on-secondary: '#ffffff'
  secondary-container: '#b2d8d8'
  on-secondary-container: '#1a2e4a'
  tertiary: '#0d7377'
  on-tertiary: '#ffffff'
  tertiary-container: '#b2d8d8'
  on-tertiary-container: '#0d7377'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  background: '#ffffff'
  on-background: '#1a1a2e'
  surface-variant: '#b2d8d8'
typography:
  h1:
    fontFamily: Calibri
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Calibri
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Calibri
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Calibri
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Calibri
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Calibri
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Calibri
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
  label-sm:
    fontFamily: Calibri
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

This design system dictates the visual styling for presentations and related artifacts. The brand personality relies on a structured, professional corporate aesthetic featuring a sleek color palette that prioritizes deep blues, light cyans, and dark slates.

## Colors

The palette is anchored by a professional **Dark Blue (#1A2E4A)** and an energetic **Light Blue (#14B0E2)**. The backgrounds remain predominantly **White (#FFFFFF)**, ensuring the deep tones stand out effectively. A series of grayish blues and cyans provide necessary depth and subtle accents without overwhelming the core content.

- **Primary:** Dark Blue (`#1A2E4A`)
- **Secondary:** Light Blue (`#14B0E2`)
- **Tertiary:** Dark Teal (`#0D7377`)
- **Background:** White (`#FFFFFF`)
- **Text (High Contrast):** Dark Slate (`#1A1A2E`)
- **Text (Medium Contrast):** Grayish Blue (`#5A6A7A`)
- **Borders & Outlines:** Gray Blue (`#6B7A8D`)
- **Subtle Backgrounds:** Light Cyan (`#B2D8D8`)

## Typography

This design system utilizes **Calibri** as the sole typeface, ensuring clean, highly legible text that perfectly matches standard professional document and presentation formatting. 

Headlines use tighter letter-spacing and heavier weights to provide clear section anchoring. Body text prioritizes a comfortable line height to facilitate scanning of content on slides.

## Layout & Spacing

The layout is designed for maximum clarity on presentation slides. The spacing rhythm is built on a 4px base unit. 
- **16px (md)** is the standard padding for blocks of text or image containers.
- **24px (lg)** is used for section gaps and layout margins.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and contrast rather than heavy shadows. 

1.  **Level 0 (Floor):** The presentation slide background is pure White.
2.  **Level 1 (Surface):** Primary content containers or highlights can use subtle fills like Light Cyan (`#B2D8D8`).
3.  **Level 2 (Interaction/Focus):** Highlighted elements use Light Blue (`#14B0E2`) to draw the eye.

## Shapes

The design system employs a **Rounded (Level 2)** shape language to slightly soften the interface and slide layouts. 

- Standard components (Buttons, Inputs, Chips, small text boxes) utilize a **0.5rem (8px)** corner radius.
- Large containers (Cards, prominent callouts) use **1rem (16px)**.

## Components

### Highlights & Accents
To draw attention to key takeaways, use the Light Blue (`#14B0E2`) or Dark Teal (`#0D7377`).

### Shapes & Boxes
Content boxes or structural elements should use Gray Blue (`#6B7A8D`) for borders.

### Cards & Sections
When visually grouping related information on a slide, a Light Cyan (`#B2D8D8`) background can be used effectively without distracting from the main text which should be Dark Slate (`#1A1A2E`).