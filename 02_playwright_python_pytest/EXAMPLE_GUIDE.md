# Demonstration guide

All commands assume the bundle directory is the current working directory and its environment is active. The local server starts automatically. Core tests require installed dependencies plus the Playwright Chromium and Firefox engines. Commands below run each browser-dependent case on both engines; the direct API example runs once because it has no browser dependency. Unnumbered expected outcomes apply to both engines. Each source file has the same introductory teaching notes followed by runnable code.

## 01. First browser test

**Achieve:** Navigate to a page and verify its title and heading.

**Time:** 6 minutes

**Source:** [test_01_first_test.py](test_01_first_test.py)

```sh
python -m pytest test_01_first_test.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** page is supplied by pytest-playwright. goto navigates. expect retries supported checks until they pass or time out. The page fixture owns browser-page cleanup.

**Expected result:** 1 passed per browser (2 total); title and heading match.

**Practice:** Change the expected title and read the failure, then restore it.

## 02. Locate by ID

**Achieve:** Fill a uniquely identified field.

**Time:** 6 minutes

**Source:** [test_02_id.py](test_02_id.py)

```sh
python -m pytest test_02_id.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** CSS #username matches id="username". IDs should be unique. locator creates a reusable query; fill replaces current text.

**Expected result:** Username contains tester.

**Practice:** Fill the password by ID.

## 03. Locate by class

**Achieve:** Use one or multiple CSS classes.

**Time:** 6 minutes

**Source:** [test_03_class.py](test_03_class.py)

```sh
python -m pytest test_03_class.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** A dot selects a class. .text-input.user-field means one element with both classes; a space would mean a descendant. Class selectors can be brittle when styling classes change.

**Expected result:** Field populated and 2 product cards found.

**Practice:** Select the sign-in button using its class.

## 04. Name, type, and attribute selectors

**Achieve:** Find elements by HTML attributes and CSS relationships.

**Time:** 6 minutes

**Source:** [test_04_attributes_css.py](test_04_attributes_css.py)

```sh
python -m pytest test_04_attributes_css.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** [name="username"] matches an exact attribute value. > selects direct children. ^= means starts with; *= means contains; $= means ends with. Name is an attribute selector, not a separate get_by_name method.

**Expected result:** Correct username, password, and submit button are found.

**Practice:** Locate username with a placeholder ends-with selector.

## 05. Role and accessible name

**Achieve:** Locate controls as an assistive technology user would.

**Time:** 6 minutes

**Source:** [test_05_role.py](test_05_role.py)

```sh
python -m pytest test_05_role.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** get_by_role combines an implicit or explicit ARIA role with its accessible name. A native button already has role button. exact=True prevents partial name matching. Prefer meaningful user-facing locators when possible.

**Expected result:** Named controls and heading are located.

**Practice:** Locate the Download report link by role.

## 06. Label and placeholder

**Achieve:** Locate form fields using their visible meaning.

**Time:** 6 minutes

**Source:** [test_06_label_placeholder.py](test_06_label_placeholder.py)

```sh
python -m pytest test_06_label_placeholder.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** get_by_label uses associated label text, including for/id associations. get_by_placeholder uses the placeholder attribute. A placeholder is not a replacement for a proper accessible label.

**Expected result:** Both fields contain expected values.

**Practice:** Fill the password using its label.

## 07. Text, alt text, and title

**Achieve:** Find messages, images, and tooltip metadata.

**Time:** 6 minutes

**Source:** [test_07_text_alt_title.py](test_07_text_alt_title.py)

```sh
python -m pytest test_07_text_alt_title.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** get_by_text matches text content, get_by_alt_text matches an alt attribute, and get_by_title matches a title attribute. A title locator does not check the document title; expect(page).to_have_title does.

**Expected result:** Message, image, and save button are found.

**Practice:** Verify the page title and explain how that differs from get_by_title.

## 08. Test IDs and XPath

**Achieve:** Compare explicit test contracts with structural selectors.

**Time:** 6 minutes

**Source:** [test_08_testid_xpath.py](test_08_testid_xpath.py)

```sh
python -m pytest test_08_testid_xpath.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** get_by_test_id defaults to data-testid and provides a deliberate testing contract. XPath selects by paths and predicates. Avoid absolute XPath tied to page layout; CSS/XPath structure can change during refactoring. XPath does not pierce shadow roots.

**Expected result:** Test ID and XPath locate the intended controls.

**Practice:** Write an XPath for the username input.

## 09. Scope, filter, and locator chaining

**Achieve:** Click the correct button when several share a name.

**Time:** 6 minutes

**Source:** [test_09_filter_scope.py](test_09_filter_scope.py)

```sh
python -m pytest test_09_filter_scope.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** Both products have an Add to cart button. A page-wide click would violate strictness because it matches twice. Filter to one product, then find the button inside it. has_text matches descendant text as well.

**Expected result:** Cart says Added Mouse.

**Practice:** Select Keyboard with filter(has=...).

## 10. Lists, nth, and tables

**Achieve:** Assert repeated items and inspect a table row.

**Time:** 6 minutes

**Source:** [test_10_lists_tables.py](test_10_lists_tables.py)

```sh
python -m pytest test_10_lists_tables.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** nth uses zero-based indexing; first and last also exist. Prefer matching item identity when order is not a requirement. to_have_text with a list checks the texts and order of the matched elements.

**Expected result:** Two products and two data rows; TC02 is FAIL.

**Practice:** Assert the first table case is PASS.

## 11. Fill, click, and assert

**Achieve:** Automate a complete login outcome.

**Time:** 6 minutes

**Source:** [test_11_login.py](test_11_login.py)

```sh
python -m pytest test_11_login.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** Use Arrange (load via fixture), Act (fill and submit), Assert (verify visible outcome). Clicking alone does not prove login worked. These credentials belong only to this local teaching site.

**Expected result:** Welcome, tester! is displayed.

**Practice:** Try a wrong password and assert the rejection message.

## 12. Checkboxes and radio buttons

**Achieve:** Set and verify state deterministically.

**Time:** 6 minutes

**Source:** [test_12_checkbox_radio.py](test_12_checkbox_radio.py)

```sh
python -m pytest test_12_checkbox_radio.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** check/uncheck set a desired state instead of blindly toggling it. Radios in the same name group are mutually exclusive. Assertions verify the resulting state.

**Expected result:** Terms end unchecked and Pro plan selected.

**Practice:** Use set_checked(True) for terms.

## 13. Native dropdowns

**Achieve:** Select by value, label, and index.

**Time:** 6 minutes

**Source:** [test_13_dropdown.py](test_13_dropdown.py)

```sh
python -m pytest test_13_dropdown.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** select_option works for native <select>. Value is the option value; label is the displayed text; index is zero-based including the placeholder. A custom dropdown built from divs requires clicking its visible controls instead.

**Expected result:** Selections are IN, GB, then IN.

**Practice:** Save preferences and check the message.

## 14. Keyboard, hover, and double click

**Achieve:** Exercise event-driven interactions.

**Time:** 6 minutes

**Source:** [test_14_keyboard_mouse.py](test_14_keyboard_mouse.py)

```sh
python -m pytest test_14_keyboard_mouse.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** press sends a key to a locator, hover moves the pointer, and dblclick triggers a double-click event. fill sets a field efficiently; use press_sequentially when per-character keyboard events are the behavior under test.

**Expected result:** Search result, hover hint, and double-click confirmation appear.

**Practice:** Replace fill with press_sequentially for the search input.

## 15. Auto-waiting and delayed UI

**Achieve:** Wait for behavior instead of sleeping.

**Time:** 6 minutes

**Source:** [test_15_auto_wait.py](test_15_auto_wait.py)

```sh
python -m pytest test_15_auto_wait.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** Actions wait for relevant actionability checks, such as visibility, stability, and enabled state. expect retries its condition. It does not magically know all background work; assert the specific completion signal. Avoid time.sleep and wait_for_timeout in normal tests.

**Expected result:** The test passes after the delayed message appears.

**Practice:** Increase the site delay to 1000 ms; rerun without changing the test and restore the site.

## 16. Confirm and prompt dialogs

**Achieve:** Register a handler before the dialog opens.

**Time:** 6 minutes

**Source:** [test_16_dialogs.py](test_16_dialogs.py)

```sh
python -m pytest test_16_dialogs.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** once registers a handler for one event. Dialog handlers must accept or dismiss; a handler that only logs leaves the action blocked. Register before clicking to avoid missing the event.

**Expected result:** 2 tests pass per browser (4 total): confirmation accepted and prompt receives Asha.

**Practice:** Dismiss confirmation and assert Cancelled.

## 17. Work inside an iframe

**Achieve:** Locate a control in a separate document.

**Time:** 6 minutes

**Source:** [test_17_iframe.py](test_17_iframe.py)

```sh
python -m pytest test_17_iframe.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** A normal page locator does not cross iframe document boundaries. frame_locator identifies the frame, then locators inside it find its content. Keep the frame selector stable and unique.

**Expected result:** Ticket submitted appears inside the frame.

**Practice:** Assert the subject value before submitting.

## 18. New tabs and popups

**Achieve:** Capture the new page event before clicking.

**Time:** 6 minutes

**Source:** [test_18_popup.py](test_18_popup.py)

```sh
python -m pytest test_18_popup.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** expect_popup waits for a new page opened by this page. The context manager arms the listener before the click, then exposes the Page through value. Each tab has its own locators.

**Expected result:** New help tab is verified and closed.

**Practice:** Assert the help paragraph.

## 19. Upload and download

**Achieve:** Provide a local file and verify downloaded content.

**Time:** 6 minutes

**Source:** [test_19_upload_download.py](test_19_upload_download.py)

```sh
python -m pytest test_19_upload_download.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** set_input_files sets a file input directly without automating the OS picker. expect_download captures the event; save_as persists the temporary download. tmp_path isolates file artifacts. This practice upload displays a filename; it does not send bytes to a backend.

**Expected result:** Filename appears and the downloaded CSV contains TC02,FAIL.

**Practice:** Clear the selected file and assert No file.

## 20. Assertions and screenshots

**Achieve:** Verify text, values, state, attributes, URL, and evidence.

**Time:** 6 minutes

**Source:** [test_20_assertions_screenshots.py](test_20_assertions_screenshots.py)

```sh
python -m pytest test_20_assertions_screenshots.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** Use web-first expect for dynamic browser state. Ordinary assert suits already returned Python values such as file sizes. A screenshot is evidence, not a visual regression assertion by itself. The URL assertion compares navigation against the independently expected lab address.

**Expected result:** Browser properties match and a nonempty PNG is saved to tmp_path.

**Practice:** Navigate to the Login section link and assert the URL ends in #login.

## 21. Data-driven login tests

**Achieve:** Run valid, invalid, and empty login inputs.

**Time:** 8 minutes

**Source:** [test_21_parametrize.py](test_21_parametrize.py)

```sh
python -m pytest test_21_parametrize.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** pytest creates one independent test for each row. Each case receives a fresh browser context through the default fixtures, so a successful login cannot leak into the next case. IDs explain which scenario failed.

**Expected result:** 3 passed per browser (6 total).

**Practice:** Add an unknown user with the correct password.

## 22. Fixtures and browser isolation

**Achieve:** Reuse setup and prove storage starts clean.

**Time:** 8 minutes

**Source:** [test_22_fixtures_isolation.py](test_22_fixtures_isolation.py)

```sh
python -m pytest test_22_fixtures_isolation.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** conftest.py defines lab_url (session server), lab (function page navigation), and logged_in_page (function login). pytest resolves fixture dependencies. The page/context fixtures isolate cookies and storage per test even though the browser process may be shared. evaluate is used here only to inspect storage.

**Expected result:** 2 passed per browser (4 total), independent of order.

**Practice:** Call Restore session in the fresh context and check its message.

## 23. Page Object Model

**Achieve:** Move repeated selectors and actions into a reusable object.

**Time:** 8 minutes

**Source:** [test_23_page_objects.py](test_23_page_objects.py)

```sh
python -m pytest test_23_page_objects.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** LoginPage in pages.py groups login locators and the sign_in action. The test keeps its assertion so the business expectation stays visible. Avoid hiding every trivial locator behind unnecessary abstractions; refactor when reuse or change warrants it.

**Expected result:** Login succeeds through the page object.

**Practice:** Use the same page object for an invalid login.

## 24. Reuse storage state

**Achieve:** Save and load browser storage into an isolated context.

**Time:** 8 minutes

**Source:** [test_24_storage_state.py](test_24_storage_state.py)

```sh
python -m pytest test_24_storage_state.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** storage_state saves cookies and local storage. It does not include sessionStorage. This lab demonstrates persistence of a demo flag, not real server-side authentication. The plugin new_context fixture creates the restored context in whichever engine is selected and manages teardown and artifacts. The test also closes it explicitly once it is finished. Real authentication-state files can contain secrets and should not be committed.

**Expected result:** A second context restores tester from saved local storage.

**Practice:** Create the second context without storage_state and expect No saved session.

## 25. Markers, selection, and test organization

**Achieve:** Run a smoke subset or a named test.

**Time:** 8 minutes

**Source:** [test_25_markers.py](test_25_markers.py)

```sh
python -m pytest test_25_markers.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** Markers group tests independently of filenames. smoke is registered in pytest.ini. -m smoke selects marked tests; -k selects names; a node ID selects one specific function. Selection changes which tests run, not their behavior.

**Expected result:** 2 passed per browser (4 total) for this file; -m smoke selects one per browser.

**Practice:** Run this file with -m smoke, then with -k table.

## 26. Observe a network response

**Achieve:** Wait for a specific request and verify UI plus payload.

**Time:** 8 minutes

**Source:** [test_26_network_response.py](test_26_network_response.py)

```sh
python -m pytest test_26_network_response.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** Arm expect_response before the click. Match the intended URL and method, inspect the response, then assert rendered content because receiving a response alone does not prove the UI used it correctly.

**Expected result:** HTTP 200, payload Asha, and Asha rendered.

**Practice:** Assert the response content-type contains application/json.

## 27. Mock an API response

**Achieve:** Make the browser render controlled test data.

**Time:** 8 minutes

**Source:** [test_27_mock_api.py](test_27_mock_api.py)

```sh
python -m pytest test_27_mock_api.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** route intercepts matching requests; fulfill supplies a fake HTTP response. Register it before the action. This tests front-end rendering under controlled data; it does not validate the real backend. Use response observation or direct API tests for that.

**Expected result:** UI renders Mock User instead of the real server value Asha.

**Practice:** Mock an empty users array and assert zero list items.

## 28. Direct API testing

**Achieve:** Check an API without a page interaction.

**Time:** 8 minutes

**Source:** [test_28_api_request.py](test_28_api_request.py)

```sh
python -m pytest test_28_api_request.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** APIRequestContext sends HTTP directly. new_context(base_url=...) supports relative API paths. dispose releases resources. This contrasts with a page triggering fetch and is useful for API checks or test setup. Browser configuration flags do not configure this manually created API context.

**Expected result:** API returns the expected JSON.

**Practice:** Check an unknown path returns HTTP 404.

## 29. Viewport and browser configuration

**Achieve:** Exercise desktop and narrow layouts.

**Time:** 8 minutes

**Source:** [test_29_viewport.py](test_29_viewport.py)

```sh
python -m pytest test_29_viewport.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** set_viewport_size changes the viewport dimensions. A narrow viewport is not full device emulation: it does not set touch, user agent, or device scale. These viewport-only checks run on both Chromium and Firefox. Full mobile emulation is not supported on Firefox. This smoke check verifies core controls at two sizes, not a complete responsive-design audit.

**Expected result:** 2 passed per browser (4 total) at desktop and narrow sizes.

**Practice:** Add a 768 by 1024 viewport case and run this file on both browsers.

## 30. Capstone user journey

**Achieve:** Combine login, preferences, product choice, and API output.

**Time:** 8 minutes

**Source:** [test_30_capstone.py](test_30_capstone.py)

```sh
python -m pytest test_30_capstone.py --browser chromium --browser firefox -v --headed --slowmo 350
```

**Explain while showing the code:** The journey stitches individually taught actions into one readable flow. Assert milestones so failures point to a meaningful stage. Keep separate focused tests as well; a long journey should not replace all smaller checks.

**Expected result:** Login, preferences, cart, and user list match their requirements.

**Practice:** Change the journey to select Mouse and United Kingdom.

## 31. Optional public website: example.com

**Achieve:** Apply locators to an external page.

**Time:** Optional extension

**Source:** [test_31_public_example.py](test_31_public_example.py)

```sh
python -m pytest test_31_public_example.py --browser chromium --browser firefox -v --headed --slowmo 350 --run-public
```

**Explain while showing the code:** This opt-in example needs internet. A public site can change independently of the test. The local examples remain the reliable classroom path.

**Expected result:** Public title and heading match; skipped unless --run-public is supplied.

**Practice:** Inspect the link by role without clicking it.

## 32. Optional public website: TodoMVC

**Achieve:** Create, complete, and remove a todo item.

**Time:** Optional extension

**Source:** [test_32_public_todomvc.py](test_32_public_todomvc.py)

```sh
python -m pytest test_32_public_todomvc.py --browser chromium --browser firefox -v --headed --slowmo 350 --run-public
```

**Explain while showing the code:** This external demo provides a realistic mini-flow. Fresh contexts isolate local storage. Its DOM is controlled by another team and may change; keep it optional and verify it before class.

**Expected result:** Todo is added, completed, and deleted; skipped by default.

**Practice:** Create a second todo and assert the two item texts.

