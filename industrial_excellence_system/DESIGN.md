---
name: Industrial Excellence System
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#3d4a3f'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#6d7a6e'
  outline-variant: '#bccabc'
  surface-tint: '#006d37'
  primary: '#006d37'
  on-primary: '#ffffff'
  primary-container: '#27ae60'
  on-primary-container: '#00391a'
  inverse-primary: '#61de8a'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#5b5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#959998'
  on-tertiary-container: '#2d3131'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#7efba4'
  primary-fixed-dim: '#61de8a'
  on-primary-fixed: '#00210c'
  on-primary-fixed-variant: '#005228'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e0e3e2'
  tertiary-fixed-dim: '#c4c7c6'
  on-tertiary-fixed: '#181c1c'
  on-tertiary-fixed-variant: '#434847'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Work Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: Work Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  headline-md:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Open Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Open Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: Work Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 1.5rem
  margin-mobile: 1rem
  section-padding: 5rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

The design system is engineered to convey reliability, precision, and industrial strength. It targets B2B stakeholders in the oil, gas, and manufacturing sectors, demanding an interface that feels both technologically advanced and physically grounded.

The visual direction follows a **Corporate / Modern** aesthetic with a strong emphasis on **Industrial Minimalism**. It prioritizes clarity and high-quality environmental photography over decorative elements. The user experience should evoke a sense of "structured efficiency"—where every element has a functional purpose and the path to technical information is unobstructed. 

Key attributes include:
- **Authority:** Through bold, high-contrast typography and large-scale imagery.
- **Transparency:** Utilized through clean, white space and systematic information architecture.
- **Precision:** Reflected in the strict grid-based alignment and fine-lined iconography.

## Colors

The color palette is grounded in neutral tones typical of industrial environments, accented by a high-visibility signal green.

- **Primary (Vibrant Green):** Reserved for primary actions (Call to Actions), active states in navigation, and critical highlights. It represents growth and operational safety.
- **Secondary (Deep Black/Gray):** Used for the footer, primary headings, and heavy text to provide a solid foundation and maximum legibility.
- **Tertiary (Industrial Gray):** A cooling light gray used for background sections, accordion headers, and subtle UI borders to prevent visual fatigue from pure white.
- **Neutrals:** A spectrum of grays used for body text and secondary metadata, ensuring a clear information hierarchy.

The default mode is **Light**, leveraging white space to maintain a clean, professional "catalog" feel.

## Typography

This design system utilizes a dual-font strategy to balance character and readability. **Work Sans** provides a geometric, sturdy feel for headlines and labels, while **Open Sans** ensures high legibility for dense technical descriptions and body copy.

Headings should employ generous letter spacing (tracking) to enhance the "industrial" look, making titles feel expansive and architectural. All-caps treatments should be reserved for small labels, breadcrumbs, and top-bar contact information to maintain a professional, organized hierarchy.

## Layout & Spacing

The layout is built on a **12-column fixed grid** for desktop, ensuring that technical specifications and large-scale imagery align with architectural precision. 

- **Vertical Rhythm:** Large vertical gaps (Section Padding) are used between major content blocks to allow the industrial imagery to "breathe" and serve as visual anchors.
- **Hero Sections:** Utilize full-bleed imagery with centered or left-aligned typography overlays.
- **Mobile Reflow:** On mobile devices, the 12-column grid collapses into a single-column stack. Section padding is reduced by 50% to maintain momentum, and horizontal margins are tightened to 16px.
- **Content Blocks:** Information is grouped into distinct horizontal bands, alternating between white and light gray backgrounds to delineate different service offerings or product categories.

## Elevation & Depth

To maintain a clean and flat industrial aesthetic, this design system avoids heavy shadows. Instead, it relies on **Tonal Layers** and **Low-contrast Outlines**.

- **Layering:** Depth is created by placing white "cards" or content containers over light gray backgrounds. 
- **Borders:** Subtle, 1px solid borders in a light gray shade (slightly darker than the background) are used to define boundaries in accordion lists and product grids.
- **Imagery:** Large photos provide the primary "depth" in the system. Masking techniques—such as organic, fluid shapes for sector images—soften the rigid grid and draw the eye to specific focal points.
- **Interaction:** Hover states on interactive elements should use a slight shift in background color or a subtle lifting effect via a very soft, diffused ambient shadow.

## Shapes

The shape language is primarily **Soft (0.25rem)**. This slight rounding takes the "edge" off the industrial rigidity, making the interface feel modern and user-friendly without losing its professional character.

- **Buttons:** Use a consistent `rounded-md` (0.25rem to 0.5rem) corner radius.
- **Accordions:** Maintain sharp outer corners for the container, but use soft internal corners for the interactive items.
- **Organic Masks:** Feature imagery (as seen in the Sectors section) uses large, custom "blob" masks to contrast against the otherwise linear and rectangular layout, adding a sophisticated, designer touch to the industrial theme.

## Components

### Navigation & Header
- **Top Bar:** A slim, high-contrast bar containing contact information (phone, email) and a language switcher.
- **Main Nav:** Transparent or white background with simple text links. The active state is indicated by the primary green color.

### Buttons
- **Primary:** Solid green background with white text. Rounded corners. High horizontal padding.
- **Secondary/Ghost:** 1px border in dark gray or white, depending on the background.

### Accordions (Product Lists)
- Clean, full-width rows with a light gray background.
- Left-aligned "+" icon for expansion.
- Hover state: Background shifts slightly darker to indicate interactivity.

### Cards & Grid Items
- **Logo Grid:** A clean 6-column grid for partner logos, each contained within a subtle light-gray bordered box to ensure visual uniformity among varied logo shapes.
- **Sector Cards:** Alternating layout of text and organically-masked imagery.

### Input Fields
- Minimalist design with a 1px bottom border or light gray stroke.
- Focus state: Border color shifts to the primary green.