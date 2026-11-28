# Locator guide — inspect, locate, act, assert

In the practice page, inspect the Username input:

```html
<label for="username">Username</label>
<input id="username" name="username" class="text-input user-field"
       placeholder="Enter username" data-testid="username-input">
```

The following locators all identify that same field. `lab` is the Page fixture returned after navigating to the local site.

| Strategy | Python | What it matches |
|---|---|---|
| ID | `lab.locator("#username")` | HTML id |
| One class | `lab.locator(".user-field")` | A class token |
| Two classes on the same element | `lab.locator(".text-input.user-field")` | Both class tokens |
| Name attribute | `lab.locator('input[name="username"]')` | Input with exact name |
| ID attribute | `lab.locator('[id="username"]')` | Exact attribute match |
| Tag plus attribute | `lab.locator('input[placeholder="Enter username"]')` | Input with exact placeholder |
| Label | `lab.get_by_label("Username", exact=True)` | Associated accessible label |
| Placeholder | `lab.get_by_placeholder("Enter username", exact=True)` | Placeholder text |
| Role | `lab.get_by_role("textbox", name="Username", exact=True)` | Role plus accessible name |
| Test ID | `lab.get_by_test_id("username-input")` | data-testid contract |
| XPath | `lab.locator('xpath=//input[@id="username"]')` | XPath predicate |

**ID syntax:** `#username` uses a hash. **Class syntax:** `.user-field` uses a dot. `input` is a tag selector. `input.user-field` means an input with that class. `.product-card button` means buttons anywhere inside the card; `.product-card > button` means direct children only.

## More CSS patterns

```python
lab.locator('input[type="password"]')        # exact attribute
lab.locator('input[placeholder^="Enter"]')   # starts with
lab.locator('input[placeholder$="username"]') # ends with
lab.locator('input[placeholder*="user"]')    # contains
lab.locator('input[name="plan"][value="pro"]') # both conditions
lab.locator('#results-table tbody tr')       # descendants
lab.locator('#login-form > button')          # direct child
lab.locator('.product-card').nth(0)          # first matching card, zero-based
lab.locator('.product-card').first           # first matching card
lab.locator('.product-card').last            # last matching card
```

Attribute substring selectors match the literal attribute string. Do not use `[class*="user"]` as a substitute for a class-token selector when `.user-field` expresses the intent precisely.

## Other built-in locators

```python
lab.get_by_text("Cart is empty", exact=True)
lab.get_by_alt_text("Testing academy logo", exact=True)
lab.get_by_title("Save preferences", exact=True)
lab.get_by_role("button", name="Sign in", exact=True)
```

Text content, image alt text, element title, and page title are different concepts. Check the document title with `expect(lab).to_have_title("Tester Practice Lab")`.

Regular expressions are also supported by many text-based locators:

```python
import re
lab.get_by_role("button", name=re.compile(r"^Sign in$", re.IGNORECASE))
```

## Multiple matches and strictness

```python
cards = lab.get_by_test_id("product-card")
expect(cards).to_have_count(2)
mouse = cards.filter(has_text="Mouse")
mouse.get_by_role("button", name="Add to cart", exact=True).click()
```

A single-element action such as click fails when more than one element matches. First scope by region, label, product name, or a stable test contract. Avoid choosing `.first` solely to suppress ambiguity; it can silently select the wrong item after reordering. Use `nth` when ordering is part of the requirement.

A descendant-based filter is useful when text could match unrelated descriptions:

```python
keyboard = cards.filter(has=lab.get_by_role("heading", name="Keyboard", exact=True))
```

The inner locator is evaluated relative to each candidate outer element and must be in the same frame.

## XPath comparison

```python
lab.locator('xpath=//input[@id="username"]')
lab.locator('xpath=//form[@id="login-form"]//button[@type="submit"]')
```

`//` selects descendants, `@` accesses an attribute, and brackets add a condition. Long absolute paths such as `/html/body/section[1]/form/input[1]` are fragile when layout changes. CSS and XPath can both be valid, but user-facing locators or explicit test IDs usually communicate intent better.

## Frames and shadow DOM

An iframe is a separate document. First select its frame:

```python
support = lab.frame_locator('iframe[title="Support frame"]')
support.get_by_label("Ticket subject", exact=True).fill("Login issue")
```

Most Playwright locators work through open shadow roots automatically. XPath does not; closed shadow roots are not supported. This bundle demonstrates an iframe; it does not include a custom shadow-DOM widget.

## Practical locator choice

Prefer the user's role/name or label when that expresses the behavior. Use test IDs for a deliberate stable testing contract. Use stable IDs or attributes when appropriate. Use class selectors carefully because styling changes frequently. Inspect the HTML and check uniqueness before writing an action. Avoid generated class names, deeply nested CSS, layout-dependent XPath, and unconditional sleeps.

Reference: [official locator guide](https://playwright.dev/python/docs/locators).
