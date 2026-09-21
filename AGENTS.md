# Rules for AI coding agents

Read this file and `requirements.md` before every task.

## 1. Scope
- Build ONLY what `requirements.md` and the current task describe. Do not invent features.
- One task = one small change = one pull request.
- Touch only the files the task lists. If more files seem needed, stop and ask.
- If anything is unclear, ask. Do not guess.

## 2. Code quality (no AI slop)
- No dead code, unused files, unused imports, or commented-out code.
- No placeholder text (lorem ipsum, "TODO", "example", fake data) in finished work.
- No duplicated code. Reuse what already exists before writing new code.
- No new dependencies without approval. If one is truly needed, explain why in the PR.
- Keep it simple. Prefer the smallest change that meets the "Done when" test.
- Remove debug logging before finishing.

## 3. Tests
- Every feature gets tests that match its "Done when" line in `requirements.md`.
- Never delete, skip, weaken, or disable a test or check to make it pass.
- Fix the root cause, not the symptom.

## 4. Security (always)
- Never write secrets, keys, or passwords in code. Use environment variables. Never commit `.env` files.
- Treat all user input as untrusted: validate it and escape output.
- Database access rules: deny by default. Allow only what `requirements.md` section 5 says.
- Never trust the browser to enforce permissions. Enforce them on the server or in database rules.
- No `eval`, no unsafe HTML injection, no disabled security headers.
- Use trusted services for login and payments. Never build those from scratch.

## 5. Mobile and speed
- Design mobile-first. Test small screens first.
- Keep pages light: compress images, avoid heavy libraries, avoid unnecessary re-renders.
- Meet the speed targets in `requirements.md` section 7.

## 6. When a check fails
- Read the error. Fix only its cause.
- Do not change unrelated files.
- Re-run all checks and report the result.
- If the same problem fails 5 times, STOP. Write down what you tried and ask for help.

## 7. Pull request description (keep it short)
- What changed (2 lines)
- How it was tested
- Any new dependency or risk
