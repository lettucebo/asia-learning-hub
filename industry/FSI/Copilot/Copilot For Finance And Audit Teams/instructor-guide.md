# Instructor guide

[Workshop home](./README.md)

Everything you need to teach the six Meridian workshops to business users: the Meridian story in plain words, a 60-minute run of show, and for every step what to say, one question to ask and what to watch for.

## Before the session

- Everyone has a Microsoft 365 Copilot licence and can sign in. Check this a day before.
- The sample files are saved in OneDrive or SharePoint, where the labs expect them. Download the ZIP from the lab and upload it. Check in your own environment that Copilot can open them.
- You have run one prompt yourself, in the app for this session, so you know what a good answer looks like.
- Outlook session: the .eml email opens in your Outlook. Teams session: the transcript is posted in a TRAINING chat only, never a real client chat.

## Suggested 60-minute run of show

The same shape for every session.

| Time | What happens | How |
| --- | --- | --- |
| 0–5 min | Welcome, the Meridian story and your role | Tell the story below, then ask the room what they know about audits. Learners read **Your role and your job today** in the lab. |
| 5–10 min | Files and setup | Learners read **Which file do you trust?**, download the files and save them in OneDrive or SharePoint. Best done before the session. |
| 10–15 min | Prompt formula and explore | Teach the one-sentence formula from the [reference](./reference.md), then let people skim the file or channel. |
| 15–20 min | Demo | Run the first prompt live so everyone sees the whole flow once, including the check. |
| 20–55 min | Hands-on: Try Out 1, Try Out 2 and Refine | About 35 minutes on the suggested times in the lab. Walk the room and use the **Check** sections to talk about answers. |
| 55–60 min | Review and takeaways | Run the six review questions, then finish on the closing question. |

> **An adaptation.** The instructor deck’s own rhythm is Scenario 5 · Concept 5 · Demos ~24 · Try Out 12–15 · Review 6–7 · Refine 3–5 · Takeaways 2. This series gives 30–40 minutes to hands-on work, so the demo time is shorter and the hands-on block follows the suggested times in each lab.

## The Meridian story

Tell this in about a minute, in your own words. Every session starts with it.

Let me introduce today’s client. Meridian is a made-up regional retailer. It sells consumer electronics and home accessories, in 18 shops across Singapore, Malaysia and Thailand, plus an online store and three distribution centres.

Last year was strange. Sales went up 20.1 percent, to SGD 151.8 million. But profit before tax fell 28.6 percent, to SGD 5.5 million. More sales, less profit. And the stock in the warehouses and the money customers owe grew even faster than sales.

A lot changed along the way. A new online-store system went live in July, the way stock is valued changed in September, and the supervisor who handled supplier payments left in October.

Meridian’s board meets on 20 February 2027. It wants its FY2026 numbers checked first. So an audit team looks at the records, asks questions, collects evidence, and reports what needs fixing.

You have just joined that team, and Copilot is your assistant. Copilot proposes. You check. In the next hour you will use Copilot in the app for your session, and learn how to spot when it gets something wrong.

**Ask:** Who has been on either side of an audit, or worked in retail, and when sales go up but profit falls, where would you look first?

**Watch for:** Point at the two numbers in the FY2026 table: sales up, profit down. Read the “words you will meet” out loud once, so nobody feels lost later. If someone asks whether Meridian is real, say no: it is fictional training data.

## Contents

- [Session 1: Word](#session-1-word)
- [Session 2: Excel](#session-2-excel)
- [Session 3: PowerPoint](#session-3-powerpoint)
- [Session 4: Outlook](#session-4-outlook)
- [Session 5: Teams](#session-5-teams)
- [Session 6: Copilot Chat](#session-6-copilot-chat)

## Session 1: Word

[Open the lab](./lab/01-word.md) · You need to get up to speed on Meridian fast, turn messy interview notes into evidence, and fix a poorly written finding.

**Words to teach:** Engagement team (The group of auditors working on one client. You have just joined it.); Finding (A problem the team spotted, written up: what happened, why it matters, what to do.); Evidence (Proof you can point to: a document, a record or a number from the files.); Inconsistency (Two places that say different things about the same fact.); Executive summary (A short note for busy leaders. Only the main points.); Source file (The document an answer came from, so you can check it.)

#### Your role and your job today _(1 min)_

**Say:** You've just joined the engagement team, so this is your first day on the job. Meridian's board wants answers by 20 February, and you have three jobs in Word. First, a client summary; second, an evidence table and one finding; third, an executive summary.

**Ask:** Which of the three jobs sounds hardest to you?

**Watch for:** Point at the table of three jobs, and say these are the only three things we'll do. Don't let anyone read Meridian’s timeline in detail. It's background.

#### Which file do you trust? _(1 min)_

**Say:** We have three Word files, and they're not equally reliable. `01_Client_Background.docx` is the client background and controls the facts; `02_Audit_Interview_Notes.docx` is only what people said; `03_Audit_Findings_Draft.docx` is a rough draft. When two files disagree, we say so. We never pick one quietly.

**Ask:** If `02_Audit_Interview_Notes.docx` says one thing and `01_Client_Background.docx` says another, which one do you trust, and what do you do next?

**Watch for:** Point at the warning for each file in the table, and at the example under the table: `02_Audit_Interview_Notes.docx` says two bank accounts have differences, `01_Client_Background.docx` and `03_Audit_Findings_Draft.docx` say three. Many learners skip the warning column.

#### Download the three Word files _(1 min)_

**Say:** Now we get the files. Download one file from the list, or take all three in the ZIP. It's all made-up data, so it's safe to download.

**Ask:** Is anyone blocked from downloading files on this computer?

**Watch for:** A locked-down laptop may block downloads. Find that out now, not at minute 20. Even better: have people do this step before the session.

#### Save all three in OneDrive _(3 min)_

**Say:** For this lab, the files need to live in OneDrive or SharePoint, so we make a folder first. Open OneDrive in your browser, create a folder called Meridian Word, and upload the three files. Your company's setup may look different, so check in your own environment.

**Ask:** Does everyone have a OneDrive they can open right now?

**Watch for:** The most common stall is a learner who saved the files in Downloads and never uploaded them. Walk the room and look for the folder on each screen.

#### The prompt formula and three habits _(2 min)_

**Say:** A prompt is just what you type to Copilot. A good one is a single sentence with seven parts: role, task, source, focus, format, limit and a check. Then keep three habits: say who it's for and the format, point at the source file, and always check the answer. Spot each part in the Meridian example.

**Ask:** Which of the seven parts do you think people forget most?

**Watch for:** Tap each part of the example as you name it. The source and the check are the two parts people skip, and they matter most. Read the ground rules aloud: no personal or client data in prompts.

#### Explore the client file _(3 min)_

**Say:** Before you ask Copilot anything, know the file yourself. Open `01_Client_Background.docx` and scan sections 4, 5 and 6: the numbers, the events and last year's findings. Notice which figures you'll need to quote exactly.

**Ask:** Which one thing in these sections would you check first?

**Watch for:** The key under the table says which rows are stated facts and which are worth checking. Look for people reading the whole document instead of three sections. Start a 3-minute timer.

#### Open Copilot in Word _(5 min)_

**Say:** This is the demo, so just watch the flow. You open the file, then open Copilot. Copilot already sees the file that is open, so there is nothing to pick. Buttons can differ, so check in your own environment before you copy me.

**Ask:** What do you think Copilot needs from you before it can answer well?

**Watch for:** Say the exact file name aloud, file 01, because similar names get mixed up. If a learner's screen looks different from the lab, that's normal.

#### Try Out 1: Get to know the client _(7 min)_

**Say:** Try 1: get to know the client. Open file 01, open Copilot, paste prompt 1 and press Send. Then paste the follow-up that asks what looks inconsistent. Use the copy button on each prompt box, so nobody mistypes.

**Ask:** Before you press Send, which three risks do you expect to see?

**Watch for:** Start a timer. The prompt must be pasted exactly as written, so look for people retyping it. Point at the copy button on each prompt box.

#### Try Out 1: Check the answer _(4 min)_

**Say:** Now check the answer. That's the real skill. Compare every figure with the file, for example revenue of SGD 151.8 million and profit before tax down 28.6 percent. Mark what the file says, and what Copilot only worked out.

**Ask:** Which bullet did Copilot work out rather than read from the file, and how can you tell?

**Watch for:** The three biggest risks are Copilot's own pick, so those bullets are inferred. Point at the status label beside each row, and don't let anyone skip the follow-up list.

#### Try Out 2: From interview notes to a finding _(8 min)_

**Say:** Try 2: turn interview notes into evidence. Open `02_Audit_Interview_Notes.docx` and ask Copilot for a table with four columns: statement, who said it, possible risk, and evidence to request. Then ask for one finding with three headings: condition, risk and recommendation.

**Ask:** Why do you think the table needs a 'who said it' column?

**Watch for:** Interview notes are raw, so the table has to stay inside what was said. Watch for anyone who accepts a number Copilot added. Fast finishers can try the optional stretch.

#### Try Out 2: Check the table and the finding _(4 min)_

**Say:** Check the table first. Match every row to the person who said it. What they said is not proof until evidence backs it up. Then check that the finding uses only facts from `02_Audit_Interview_Notes.docx`.

**Ask:** Which row would you ask for evidence on first?

**Watch for:** Every row should still show the Unresolved label. Point at the warning: 'about 430' is what someone said, not a counted number. Look for any invented number, name or date.

#### Optional stretch: Rewrite finding F-02 _(Optional · 3 min)_

**Say:** This one is optional, for people who finish early. Open `03_Audit_Findings_Draft.docx`, pick finding F-02, and ask Copilot to rewrite it in neutral, professional language with a risk rating. A rating is a judgement. Copilot can propose one, and you decide.

**Ask:** Would you accept the rating Copilot proposes? What would you need to see first?

**Watch for:** There's no timer and no pressure, so don't let it slow the main group. The proposed rating is labelled as a proposal in the example, and the blank date stays visible.

#### Refine: Write the executive summary _(6 min)_

**Say:** Refine: write the executive summary. Open `03_Audit_Findings_Draft.docx` and paste the Refine prompt. It asks for the three biggest matters, how much money is at risk and what evidence is still missing, in under 150 words. Then paste the follow-up that asks Copilot to list anything it can't support.

**Ask:** What would a busy leader want from 150 words?

**Watch for:** This step is mandatory. The word limit is the point, so look for summaries that run long. The follow-up is where a first answer becomes a checked answer.

#### Refine: Check the summary _(3 min)_

**Say:** Now check the summary against `03_Audit_Findings_Draft.docx`, line by line. Only one finding has an amount, SGD 1.25 million, so any bigger total is made up. Remove anything you can't support.

**Ask:** Which sentence in the summary could you not point to in `03_Audit_Findings_Draft.docx`?

**Watch for:** Point at the date warning: `03_Audit_Findings_Draft.docx` gives finding F-05 a target date of 28 February 2027, but the board meets on 20 February. We flag it. We don't fix it quietly.

#### Review: The six questions _(2 min)_

**Say:** Last check: the six questions. Source, evidence, status, audience, action and professional boundary. Ask them of every result you plan to use. Finishing the checks doesn't approve the result, because a person decides.

**Ask:** Which of the six questions would catch the mistake you are most likely to make?

**Watch for:** 'Professional boundary' is the one people don't know. It means no audit opinion and no claim that management agreed. Point at that row. This step is mandatory.

#### What you learned today _(2 min)_

**Say:** Today you did three things with Copilot in Word. You briefed yourself on a client, turned interview notes into evidence, and wrote a summary you checked. Keep three habits: check against the source, keep the gaps visible, and let a person decide.

**Ask:** Which document at work could you check this week, using the six questions?

**Watch for:** Leave the closing question up and let people answer. Point at the link to the next session. Say it once more: Copilot proposes, the team verifies.

## Session 2: Excel

[Open the lab](./lab/02-excel.md) · Meridian posted 1,800 journal entries in FY2026. Some of them are not what they seem. Find them.

**Words to teach:** Journal entry (One line in the company’s accounting records, in the General_Ledger sheet. Meridian has 1,800.); Manual journal (An entry typed in by a person, not created automatically by a till, online shop or system.); Self-approved (The same person prepared and approved the entry, so no second person signed it off.); Flag (A marker that says look here. It is a pointer for checking, not proof of anything.); Related party (A business closely linked to the company or its leaders. Deals with it get extra checking.); Dormant vendor (A supplier marked as inactive. A payment to one needs a good explanation.)

#### Your role and your job today _(1 min)_

**Say:** You've just joined the engagement team. Meridian posted 1,800 journal entries in FY2026, which means 1,800 lines in its accounting records. You have three jobs: build flags you can check, make a shortlist of odd entries, then pick a top five.

**Ask:** What would make an entry look odd to you, even before we start?

**Watch for:** Let people answer freely: round numbers, late at night, one person doing everything. Their own ideas come back in Try Out 4. Don't let anyone read the background line by line.

#### Which file do you trust? _(1 min)_

**Say:** There are two Excel workbooks, and only workbook 04 is on the main path. Workbook 05 is a tax stretch for anyone who finishes early. Read the warning at the bottom: interview notes say about 430 manual journals in December, but this workbook shows 51, so we say so and ask for the full list.

**Ask:** When two sources disagree like that, what do you do next?

**Watch for:** Point at the warning for each file in the table and at the 430 versus 51 example. Many learners skip the warning column.

#### Download the Excel workbooks _(1 min)_

**Say:** Download workbook 04, or take both in the ZIP. It's all made-up data, so it's safe to download. Workbook 05 is only for the optional tax stretch.

**Ask:** Is anyone blocked from downloading files on this computer?

**Watch for:** A locked-down laptop may block downloads. Find that out now, not at minute 20. Even better: ask people to do this step before the session.

#### Save them in OneDrive, AutoSave on _(3 min)_

**Say:** This lab says Copilot in Excel needs the workbook saved in OneDrive or SharePoint with AutoSave on, so we make a folder first. Open OneDrive in your browser, create a folder called Meridian Excel and upload the files. Your company's setup may look different, so check in your own environment.

**Ask:** Does everyone have the workbook sitting in a OneDrive folder right now?

**Watch for:** The usual stall is a workbook still in Downloads. Walk the room and look for the folder on each screen. Ask people to check AutoSave in their own environment.

#### The prompt formula and three habits _(2 min)_

**Say:** A prompt is just what you type to Copilot. A good one is a single sentence with seven parts: role, task, source, focus, format, limit and a check. Keep three habits: say who it's for and the format, point at the source, and always check the answer.

**Ask:** Which of the seven parts do you think people forget most?

**Watch for:** Tap each part of the example as you name it. In the lab the source is a sheet name, and the check matters most. Read the ground rules aloud: no personal or client data in prompts.

#### Explore the workbook _(3 min)_

**Say:** Before you ask Copilot anything, know the workbook yourself. Skim the General_Ledger, Vendors, Employees and Expenses sheets. General_Ledger is the list of 1,800 journal entries. Note three things you could build a flag from, such as who prepared and approved an entry, and when it was posted.

**Ask:** Which one thing in these sheets would you check first?

**Watch for:** Point at the rows marked 'worth checking': Prepared By and Approved By, Posting Time and the two vendor flags. Audit_Findings is empty on purpose, because learners fill it later. Start a 3-minute timer.

#### Open Copilot in Excel _(5 min)_

**Say:** This is the demo, so just watch the flow. You open the workbook, then open Copilot. Copilot already sees the workbook that is open, so there is nothing to pick. Buttons can differ, so check in your own environment before you copy me.

**Ask:** What does Copilot need from you before it can answer well?

**Watch for:** Pause and say the exact name aloud: `04_Audit_Analytics.xlsx`. If a learner's screen looks different from the lab, that's normal.

#### Try Out 3: Flag risky journals _(7 min)_

**Say:** Try Out 3: flag risky journals. Open the General_Ledger sheet, click Copilot and paste prompt 1. It adds two Yes or No columns, Self_Approved and Late_Posting. Then paste the follow-up that asks how many Manual journals are both self-approved and late.

**Ask:** Before you press Send, how many Manual journals do you expect to be both?

**Watch for:** Start a 7-minute timer. Use the copy button on each prompt box, so nobody mistypes. Copilot may write different formulas from the lab, and that's exactly why the next step is checking.

#### Try Out 3: Check the flags _(4 min)_

**Say:** Now check the flags, row by row. Filter Self_Approved for Yes and you should get 2 rows, then filter Manual and late and you should get 41. Only one journal is both, JRN-000002 for 99,900, and remember that a flag is a pointer, not a conclusion.

**Ask:** Which row would you open first to see whether a flag is right?

**Watch for:** JRN-000397 posts at exactly 20:00, so Late_Posting should say No. That is the edge case to point at. Posting Time is text, so check the formula reads it correctly.

#### Try Out 4: Hunt for exceptions _(8 min)_

**Say:** Try Out 4: hunt for exceptions. Paste prompt 1 to find the same amount paid to the same vendor on the same day, amounts just under SGD 25,000, and round-number manual entries in December. Then paste the follow-up that looks up each vendor and flags dormant or related-party ones.

**Ask:** Why might three payments just under a limit deserve a second look?

**Watch for:** Start a 8-minute timer. Keep the Vendors sheet open. It is easy to flag too much, so remind people that Copilot proposes and they verify.

#### Try Out 4: Verify the shortlist _(4 min)_

**Say:** Check the shortlist. It's a place to start looking, not a list of problems. For example, add the three 24,950 amounts and you should get 74,850, and confirm the two 100,000 payments to V0007 on 15 December really are in the sheet. The vendor lookup also matches 101 journals for V0005 and 112 for V0006, mostly small, so filter by amount first.

**Ask:** Which item on the shortlist would you challenge first, and what would you ask for?

**Watch for:** Point at the Unresolved labels and at the warning about 101 and 112 matches. A vendor flag isn't a finding. JRN-000922, at 24,548.54, is also just below 25,000, so ask whether that is a pattern.

#### Optional stretch: Expenses duplicates _(Optional · 3 min)_

**Say:** This one is optional, for people who finish early. Open the Expenses sheet and ask Copilot for duplicate claims, and claims approved by the person who submitted them. The same rule applies: they are warning signs to check, not proof.

**Ask:** Two claims for 18,420 on the same day: a duplicate, or two real costs?

**Watch for:** There's no timer, so keep the main group moving. EXP-00001 has no receipt and is self-approved, while EXP-00002 has a receipt and a different approver. JRN-000006 has the same date and amount, so don't add them together.

#### Refine: Prioritise your top 5 _(6 min)_

**Say:** Refine: prioritise your top five. Open the Audit_Findings sheet, click Copilot and paste the Refine prompt. It asks for five exceptions, each with Journal ID, amount, why it's unusual and the evidence to request. Then paste the follow-up and copy your top five into the sheet.

**Ask:** What would you want next to each item before you could defend it to your manager?

**Watch for:** This step is mandatory. Look for lists with no evidence request. Keep the answers closed: they are for the next step, after learners have tried.

#### Refine: Check, then reveal the answers _(3 min)_

**Say:** Check your top five first: every row needs a reason and an evidence request. Only then open the Trainer_Answer_Key sheet, which is a comparison, not a verdict. Explain every difference, whether you missed an item or added an extra one.

**Ask:** What's one item in your list that the answers don't have, and why did you keep it?

**Watch for:** Don’t open the Trainer_Answer_Key sheet for them. Keep it closed until learners have tried. Look for wording like 'unusual', not 'someone did wrong'.

#### Review: The six questions _(2 min)_

**Say:** Last check: the six questions. Source, evidence, status, audience, action and professional boundary. Ask them of every result you plan to use. Finishing the checks doesn't approve the result, because a person decides.

**Ask:** Which of the six questions would catch the mistake you are most likely to make?

**Watch for:** 'Professional boundary' is the one people don't know. It means no conclusion that anyone did something wrong, and no audit opinion. Point at that row. This step is mandatory.

#### Optional stretch: Classify the tax adjustments _(Optional · 4 min)_

**Say:** This is an optional tax stretch, for anyone with time left. It uses fictional, simplified assumptions. They are not tax law and not filing advice. Go through each adjustment and say whether you'd add it back, deduct it or leave it alone, then compare with the workbook.

**Ask:** Which adjustment would you want evidence for before you rely on it?

**Watch for:** Keep the boundary warning in view the whole time. The suggested prompt is labelled 'Suggested, not from the course pack'. Five of the ten adjustments lack complete evidence, and four of them become the review points in Review_Summary.

#### Optional stretch: Follow the tax computation _(Optional · 3 min)_

**Say:** Optional again: follow the numbers from accounting profit to the tax figure. Net adjustments of minus 145,000 give 5,355,000, times 17 percent gives 910,350, and a 75,000 training tax credit leaves 835,350. These are training numbers from the workbook, not tax advice.

**Ask:** If the credit were missing, what would the tax figure be?

**Watch for:** Point at the credit line. The Assumptions sheet lists a 2.5 donation multiple and a 20% capital-allowance rate that the formulas don't apply, so verify any Copilot recalculation against the sheet.

#### Optional stretch: Write the review points _(Optional · 4 min)_

**Say:** Optional last part: write a conclusion and a next action for the four areas with incomplete evidence. There is a suggested prompt if you want Copilot to draft them, then rewrite in your own words. Each next action names the evidence still needed, and no tax opinion.

**Ask:** Which of the four areas would you chase first, and why?

**Watch for:** The prompt is labelled 'Suggested, not from the course pack'. Copilot's draft is a starting point, so learners should still check each evidence item against the sheet. Learners can write their own, then compare with the illustrative example in the lab. The 640,000 related-party fee here is a different figure from the 99,900 invoice in the main workbook, so don't equate them.

#### What you learned today _(2 min)_

**Say:** Today you used Copilot in Excel three ways. You flagged risky journals with formulas you could check, hunted for exceptions, and picked a top five with evidence to request. Keep three habits: verify every row, treat flags as pointers, and let a person decide.

**Ask:** Which spreadsheet at work could you test with a flag column, and check row by row, this week?

**Watch for:** Leave the closing question up and let people answer. Say it once more: Copilot proposes, the team verifies.

## Session 3: PowerPoint

[Open the lab](./lab/03-powerpoint.md) · Senior management wants a short briefing on the engagement status and the matters that need their attention. Turn the findings into a clear executive presentation.

**Words to teach:** Executive briefing (A short deck for leaders. A few slides, one clear message each.); Finding (A problem the team spotted, written up: what happened, why it matters, what to do.); Rating (How serious a finding is: High, Medium or Low. Some are blank in the draft.); Owner and target date (The person who will fix a finding, and the day they promise to do it.); Related party (A person or company linked to Meridian, so deals with them need extra care.); Speaker notes (Private words under a slide that help the presenter. The audience does not see them.)

#### Your role and your job today _(1 min)_

**Say:** You've just joined the engagement team, and senior management wants a short briefing. Your job is to turn the draft findings into a clear executive deck. There are three jobs: build five slides, make them boardroom-ready, then challenge the deck.

**Ask:** What would a board member want from five slides?

**Watch for:** Point at the three jobs and say these are the only three things we'll do. Don't let anyone read Meridian’s timeline in detail. It's background.

#### Which file do you trust? _(1 min)_

**Say:** We have three files, and they're not equally reliable. `03_Audit_Findings_Draft.docx` is the draft findings and `01_Client_Background.docx` is the client background; `06_Supporting_Documents.pdf` is the supporting PDF. When two files disagree, we say so. We never pick one quietly.

**Ask:** If two files give different dates for the same job, what do you do?

**Watch for:** Point at the warning for each file in the table, and at the example under the table: `03_Audit_Findings_Draft.docx` gives F-01 a target date of 15 February, but `06_Supporting_Documents.pdf` asks for dispatch evidence by 10 February. Many learners skip the warning column.

#### Download the three files _(1 min)_

**Say:** Now we get the files. Download one file from the list, or take all three in the ZIP. It's all made-up data, so it's safe to download.

**Ask:** Is anyone blocked from downloading files on this computer?

**Watch for:** A locked-down laptop may block downloads. Find that out now, not at minute 20. Even better: have people do this step before the session.

#### Save all three in OneDrive _(3 min)_

**Say:** For this lab, the files need to live in OneDrive or SharePoint, so we make a folder first. Open OneDrive in your browser, create a folder called Meridian PowerPoint, and upload the three files. Your company's setup may look different, so check in your own environment.

**Ask:** Does everyone have a OneDrive they can open right now?

**Watch for:** The most common stall is a learner who left the files in Downloads. Walk the room and look for the folder on each screen.

#### The prompt formula and three habits _(2 min)_

**Say:** A prompt is just what you type to Copilot. A good one is a single sentence with seven parts: role, task, source, focus, format, limit and a check. For slides, the limit matters most. Say how many slides and how many bullets.

**Ask:** Which of the seven parts do you think people forget most?

**Watch for:** Tap each part of the example as you name it. The source and the check are the two parts people skip. Read the ground rules aloud: no personal or client data in prompts.

#### Explore the findings and the evidence _(3 min)_

**Say:** Before you build slides, know the sources yourself. Open `03_Audit_Findings_Draft.docx` and `06_Supporting_Documents.pdf` and notice what is given, what is doubtful and what is missing. A slide must never fill a gap with a guess.

**Ask:** Which gap in the draft would worry you most in front of a board?

**Watch for:** The key under the table says which rows are stated facts, which need a check and which are missing. Look for people reading every page. Start a 3-minute timer.

#### Open Copilot in PowerPoint and find your file _(5 min)_

**Say:** This is the demo, so just watch the flow. You start a presentation, click Copilot, and type a forward slash to point Copilot at a file. Buttons can differ, so check in your own environment before you copy me.

**Ask:** Why does Copilot need your file before it can build good slides?

**Watch for:** Pause at the file picker and say the exact file name aloud, because similar names get mixed up. If a learner's screen looks different from the lab, that's normal.

#### Try Out 5: Build the executive briefing _(7 min)_

**Say:** Try Out 5: build the executive briefing. Open Copilot, paste prompt 5 and press Send. It asks for five slides, four bullets at most on each. Then paste the follow-up for a table of all six findings.

**Ask:** Before you press Send, which three findings do you expect on the Top 3 slide?

**Watch for:** Start a timer. The prompt must be pasted exactly as written, so look for people retyping it. Point at the copy button on each prompt box.

#### Try Out 5: Check the five slides _(2 min)_

**Say:** Now check the slides. That's the real skill. Match every amount and date to `03_Audit_Findings_Draft.docx`, for example the SGD 1.25 million journal posted on 31 December. Count the bullets too: four at most on a slide.

**Ask:** Which figure on the slides could you not trace back to `03_Audit_Findings_Draft.docx`?

**Watch for:** `03_Audit_Findings_Draft.docx` has no revenue or profit totals. If a slide shows them, they came from `01_Client_Background.docx`, so trace them. Point at the check list and the warning column.

#### Try Out 5: Check the findings table _(2 min)_

**Say:** Now check the table of six findings. `03_Audit_Findings_Draft.docx` leaves some ratings, owners and dates blank, and the table must show them as missing. A neat table is not a complete table.

**Ask:** What would go wrong if Copilot filled a blank owner with a guess?

**Watch for:** Point at the yellow missing flags: ratings for F-02 and F-05, the owner for F-04, and dates for F-02 and F-04. Also point at the warning: F-05's date of 28 February is after the 20 February board.

#### Try Out 6: Make it boardroom-ready _(8 min)_

**Say:** Try Out 6: make it boardroom-ready. Paste prompt 6 to rewrite the summary slide for a busy CFO: one headline sentence and three bullets, each with an amount. Then paste the follow-up that adds a slide on the related-party logistics arrangement from the PDF.

**Ask:** Why would a CFO want an amount in every bullet?

**Watch for:** Less text must not mean more claims. Fast finishers can try the optional speaker-notes stretch. Watch for anyone who accepts a slide that says approved or signed.

#### Try Out 6: Check the two slides _(4 min)_

**Say:** Check the CFO slide first. Every amount must be in `01_Client_Background.docx`, `03_Audit_Findings_Draft.docx` or `06_Supporting_Documents.pdf`. On the related-party slide, say what is missing, not what you suspect.

**Ask:** Which statement on the new slide is a fact, and which is only a worry?

**Watch for:** The invoice for SGD 99,900 is dated 31 December and the declaration is not shown. A missing declaration does not prove anything. Remove words like approved, signed or fairly priced.

#### Optional stretch: Speaker notes under 60 words _(Optional · 3 min)_

**Say:** This one is optional, for people who finish early. Ask Copilot for speaker notes under 60 words on every slide. Notes should say what the slide says, in the speaker's own voice. They must not add facts.

**Ask:** Could you say each note out loud in your own voice?

**Watch for:** There's no timer, so don't let it slow the main group. Look for a note that adds a fact the slide does not show.

#### Refine: Challenge your deck _(6 min)_

**Say:** Refine: challenge your own deck. Paste the Refine prompt. It asks Copilot to review the deck as a sceptical board member and suggest three improvements. Then paste the follow-up to apply the one improvement that matters most.

**Ask:** What is the first question a sceptical board member would ask you?

**Watch for:** This step is mandatory. Copilot suggests three improvements, but you choose one. Look for learners who try to apply all three.

#### Refine: Check the challenge _(3 min)_

**Say:** Now choose one improvement and say why it matters. A sceptic finds the gaps, and you decide which one helps the board most. Then check the whole deck again, not only the slide you changed.

**Ask:** Which improvement did you pick, and why does it help the board decide?

**Watch for:** Point at the warning to write down the improvement and the reason. Also look for a change that touched slides it should not have, or moved an amount or a date.

#### Review: The six questions _(2 min)_

**Say:** Last check: the six questions. Source, evidence, status, audience, action and professional boundary. Ask them of your final deck. Finishing the checks doesn't approve the deck, because a person decides.

**Ask:** Which of the six questions would catch the mistake you are most likely to make?

**Watch for:** 'Professional boundary' is the one people don't know. It means no audit opinion, no 'approved' and no completion claim. Point at that row. This step is mandatory.

#### What you learned today _(2 min)_

**Say:** Today you did three things with Copilot in PowerPoint. You built an executive briefing, made it boardroom-ready, and challenged it like a sceptical board member. Keep three habits: check against the source, keep the gaps visible, and let a person decide.

**Ask:** Which update could you send this week that a sceptical board member would test?

**Watch for:** Leave the closing question up and let people answer. Point at the link to the next session. Say it once more: Copilot proposes, the team verifies.

## Session 4: Outlook

[Open the lab](./lab/04-outlook.md) · The Finance Director has sent a long, urgent email about year-end evidence and the 20 February board deadline — with three attachments. Work out what matters and reply.

**Words to teach:** Evidence request (An item asking the client for a document or record that proves something. `06_Supporting_Documents.pdf` lists six.); Board meeting (The meeting of Meridian's top decision-makers on 20 February 2027. The audit should finish before it.); Blocked item (Stuck until the evidence it needs arrives. The email never says "blocked"; you work that out.); Unsupported (Not backed by the email or a file. Leave it flagged, and never fill it in.); Diplomatic tone (Polite, team-minded wording that still keeps the ask and the date clear.); Draft (A reply that is saved but not sent. Nobody sees it until a person decides to send it.)

#### Your role and your job today _(1 min)_

**Say:** You've just joined the engagement team, the group that checks Meridian's accounts. Today you do three jobs: summarise the email, build an action table, and draft a reply. The reply is saved as a draft and never sent.

**Ask:** Which of the three jobs would save you the most time on a normal Monday?

**Watch for:** Point at the table of three jobs. Skip Meridian’s timeline, because it's background. Say the boundary once: a draft only, never sent.

#### Which file do you trust? _(1 min)_

**Say:** We have one email and three attachments, and each is the right source for something different. `01_Client_Background.docx` is the client background and controls the facts. `03_Audit_Findings_Draft.docx` is a rough draft of findings, and `06_Supporting_Documents.pdf` holds the evidence request list.

**Ask:** If two files give different dates, what do you do?

**Watch for:** Point at the example under the table: `06_Supporting_Documents.pdf` says the inventory sheets are due 14 February, but the email says evidence by 12 February. Do not pick one. Ask which date applies.

#### Download the email and its three attachments _(1 min)_

**Say:** Now download the files. Download one file from the list, or take all four in the ZIP. It's all made-up data, and nothing is sent anywhere.

**Ask:** Can everyone download and open an email file on this computer?

**Watch for:** A locked-down laptop may block downloads or .eml files. Find that out now, not at minute 20. Better still, send the files before the session.

#### Open the Meridian email in Outlook _(3 min)_

**Say:** Your instructor sends you the Meridian email. If it hasn't arrived, open the .eml file from the ZIP. An .eml file is just a saved copy of an email. Check in your own environment how your Outlook opens it.

**Ask:** Is the Meridian email open on your screen, with its three attachments?

**Watch for:** The usual stall is a learner who has the file but never opened it, or an .eml that opens in the wrong app. Walk the room and look for the subject line starting "Meridian FY2026" and the three attachments.

#### The prompt formula and three habits _(2 min)_

**Say:** A prompt is what you type to Copilot. A good one is a single sentence with seven parts: role, task, source, focus, format, limit and a check. Keep three habits: say who it's for and the format, point at the source, and always check the answer.

**Ask:** Which of the seven parts do you think people forget most?

**Watch for:** Tap each part of the example as you name it. The source and the check are the two people skip, and they matter most. Read the ground rules aloud: no personal or client data in prompts.

#### Explore the email and its attachments _(3 min)_

**Say:** Before you ask Copilot, know the email yourself. Read it, then scan `03_Audit_Findings_Draft.docx` and the evidence request list in `06_Supporting_Documents.pdf`. Notice what's missing. For example, the email gives no reply-by date.

**Ask:** What is one thing in these three tables you would check first?

**Watch for:** The key under the table says which rows are stated, worth checking, or missing. Point at the F-04 row: no owner and no date. Look for people reading whole files instead of the tables, and start the 3-minute timer.

#### Open Copilot in Outlook _(5 min)_

**Say:** This is the demo, so just watch the flow. You open the email, click Copilot, and ask a question about it. The Microsoft Learn sources say Copilot can summarise Word and PDF attachments in Outlook on the web and the new Outlook for Windows. Check in your own environment.

**Ask:** What does Copilot need from you before it can answer well?

**Watch for:** Pause at the Copilot button and say where it is. If a learner's screen looks different from the lab, that's normal.

#### Try Out 7: What does this email need from me? _(7 min)_

**Say:** Try Out 7: ask Copilot what this email needs from you. Open the email, click Copilot, paste prompt 1 and press Send. Then paste the follow-up, which asks for a table with action, owner, due date and evidence needed. Use the copy button on each prompt box, so nobody mistypes.

**Ask:** Before you press Send, which owner or due date do you expect Copilot to find in the email?

**Watch for:** Start a 7-minute timer. Look for people retyping the prompt instead of pasting it. Where you type the follow-up can differ by Outlook version, so check in your own environment.

#### Try Out 7: Check the summary _(2 min)_

**Say:** Now check the summary. That's the real skill. Find where each point comes from: the email or `06_Supporting_Documents.pdf`. Mark anything Copilot only worked out, like which items are blocked.

**Ask:** Which point did Copilot work out rather than read, and how can you tell?

**Watch for:** The email never says 'blocked'. That is inferred from Open and Partial in `06_Supporting_Documents.pdf`. The email says 'several items'; the 4 Open and 2 Partial come from `06_Supporting_Documents.pdf`. Point at the source tag beside each row.

#### Try Out 7: Check the action table _(2 min)_

**Say:** Now the action table. The email names no owners and no due dates for the six items. Those come from `06_Supporting_Documents.pdf`, the evidence request list. If no source gives one, leave it marked unsupported, and never fill it in.

**Ask:** The last row is 'Reply to the Finance Director'. Why is its due date marked unsupported?

**Watch for:** Point at the ER-05 row: inventory count and ageing, due 14 Feb, after the 12 Feb condition. It is flagged. We flag it, and we do not fix it quietly.

#### Try Out 8: Reply with the right tone _(8 min)_

**Say:** Try Out 8: reply to the Finance Director. Click Reply, then Copilot and Draft with Copilot, and paste prompt 1. It asks for a firm reply under 150 words that lists the three most urgent items. Then paste the follow-up, which asks for a more diplomatic tone and a 30-minute call this Thursday.

**Ask:** What makes a reply firm but still friendly?

**Watch for:** Start a 8-minute timer. Where the Draft with Copilot button appears can differ by Outlook version, so check in your own environment. Fast finishers can try the optional Coaching stretch.

#### Try Out 8: Check the firm draft _(2 min)_

**Say:** Read the firm draft the way the Finance Director would. Look for one ask, the 12 February date, and three items. Copilot picked three of the six and the email doesn't rank them, so that choice is yours to confirm.

**Ask:** Which three items would you have picked, and why?

**Watch for:** Check the word count: under 150. Look for any sentence that promises the audit will be finished. The only promise allowed is the conditional one: on time if the evidence arrives by 12 February.

#### Try Out 8: Check the diplomatic draft _(2 min)_

**Say:** Now the diplomatic version: softer, but still clear. The ask and the 12 February date must still be there. It proposes a Thursday call. The sources give no date for that Thursday, so none gets added.

**Ask:** Would you send this one, or change a word first?

**Watch for:** The common slip is a polite draft that drops the ask. Point at the sentence with 12 February. Then point at Thursday: nobody should add a date or a time.

#### Optional stretch: Coaching by Copilot _(Optional · 3 min)_

**Say:** This one is optional, for people who finish early. Open Coaching by Copilot on your draft and apply one suggestion, not all three. Coaching suggests, and you decide. Check the exact steps in your own environment.

**Ask:** Which suggestion would you apply, and which would you ignore?

**Watch for:** There is no timer, so do not let it slow the main group. The suggestions in the lab are an illustrative example. After the edit, check that every fact from the email is still there.

#### Refine: Close the gaps _(6 min)_

**Say:** Refine means checking Copilot's first answer and fixing it. Open your draft, click Copilot and paste the Refine prompt. It asks whether your reply answers every question and request. Then paste the follow-up, which asks to fix the gaps and save the reply as a draft, not send it.

**Ask:** Which request in the email is the easiest to miss when you write a reply?

**Watch for:** This step is mandatory. Start a 6-minute timer. Look for any cursor near Send, and remind everyone: do not send. Whether Copilot can save the draft for you, check in your own environment.

#### Refine: Check the gaps _(2 min)_

**Say:** Read what Copilot says the reply missed. The email asked you to confirm what can be completed, what is blocked, and whether a call is needed. The reply missed the first two. Then run the seven checks.

**Ask:** Which gap would the Finance Director notice first?

**Watch for:** Point at the date row: ER-05 is due 14 February, after the 12 February condition, and the reply never raised it. We raise it, and we don't hide it. This step is mandatory.

#### Refine: Save the draft. Do not send. _(1 min)_

**Say:** Last step of Refine: save the reply as a draft. Do not click Send. A draft is a reply nobody sees until a person decides to send it.

**Ask:** Where would you look to confirm the reply is in Drafts and not in Sent Items?

**Watch for:** Point at the big Do not send marker and the three checks. This is the most important habit in the session. The reply still has a placeholder name, so it is not ready to send anyway.

#### Review: The six questions _(2 min)_

**Say:** Last check: the six questions. Source, evidence, status, audience, action and professional boundary. Ask them of every result you plan to use. Finishing the checks doesn't approve the result, because a person decides.

**Ask:** Which of the six questions would catch the mistake you are most likely to make?

**Watch for:** 'Professional boundary' is the one people don't know. For this email it means no promise that the audit will finish, and no claim that anyone agreed. Point at that row. This step is mandatory.

#### What you learned today _(2 min)_

**Say:** Today you did three things with Copilot in Outlook. You summarised a long email, built an action table with the gaps showing, and drafted a reply that you saved but never sent. Keep three habits: check against the source, mark what's unsupported, and let a person decide.

**Ask:** Which long email at work could you turn into an action table this week, and which owner or date would you check first?

**Watch for:** Leave the closing question up and let people answer. Point at the link to the next session. Say it once more: Copilot proposes, and you check.

## Session 5: Teams

[Open the lab](./lab/05-teams.md) · You were away for three days. The Meridian engagement chat kept moving. Catch up and prepare for tomorrow’s status meeting.

**Words to teach:** Catch-up summary (A short recap of a busy chat: what was decided, what is open, who owns what.); Citation (A link from a point in the summary back to the exact message it came from.); Open item (Something still unresolved: evidence not yet received, a question not yet answered.); Action owner (The one named person responsible for an action. No name means no owner.); Status meeting (A short meeting to check progress on open items with the client. Tomorrow’s lasts 30 minutes.); Training chat (A practice chat with fictional data only. Never a real client or team conversation.)

#### Your role and your job today _(1 min)_

**Say:** You were away for three days, and the engagement channel kept moving. Revenue evidence, duplicate payments, inventory, a related-party logistics invoice, system access, tax questions and deadlines were all discussed. Your three jobs: catch up with cited summaries, prepare tomorrow's 30-minute meeting, and complete the action list.

**Ask:** When you return to a busy chat, what do you usually do first?

**Watch for:** Point at the three jobs and say these are the only three things we'll do. The seven topics are background. Nobody needs to memorise them.

#### What is in the channel, and how far to trust it _(2 min)_

**Say:** There's no file in this session: your source is the channel itself, with three days, seven topics and 25 messages. Not every message is proof, because people report what they believe. A summary is only as good as the messages it cites, so when two messages disagree, we say so.

**Ask:** If the Finance Director says 'commercial terms' but there's no contract, is that a fact or a claim?

**Watch for:** Point at the warning for each file in the table, and at the example: the draft finding F-05 has a target date of 28 February, but the board meets on 20 February. It's a flagged conflict, not something we fix quietly.

#### Get the channel as a text file _(1 min)_

**Say:** This step is for the facilitator. Copilot in Teams needs a real conversation to read, so download the transcript and post it into a training chat, never a real one.

**Ask:** Who can set up a training chat for the group?

**Watch for:** Say clearly: fictional data, training chat only.

#### Open the channel in a training chat _(3 min)_

**Say:** The idea is simple: paste the transcript text into a training chat so Copilot has a conversation to read. Your company's setup may differ, so check in your own environment, and ask your admin if you're unsure.

**Ask:** Do you have a safe place at work for a training chat, away from real clients?

**Watch for:** The common slip is a facilitator posting the text into a real client channel. Look at the chat title: it should say Training chat (fictional).

#### Learn the prompt formula and three habits _(2 min)_

**Say:** A prompt is just what you type to Copilot. A good one is a single sentence with seven parts: role, task, source, focus, format, limit and a check. Today the source is a conversation, so ask for citations and keep the three habits: be specific, name the source, check the answer.

**Ask:** Which of the seven parts do you think people forget most?

**Watch for:** Tap each part as you name it. The source and the check are the two that people skip. Read the ground rule aloud: no real client data in prompts.

#### Read the channel before you ask _(3 min)_

**Say:** Before you ask Copilot, read the channel yourself. Scan the three days and mark three kinds of message: one with a clear owner and date, one that's only a claim, and one that shows a gap. Then you'll know what a good summary should say.

**Ask:** Which message have you marked as a gap, and why?

**Watch for:** The key under the table explains the three row types. Look for learners reading every message. Ask for just three marks. Start a 3-minute timer.

#### Open Copilot in the channel _(4 min)_

**Say:** This is the demo, so just watch the flow. You open the channel, then click Copilot, then click the box where you type. There's no file to attach here, because the conversation is the source, and buttons can differ, so check in your own environment.

**Ask:** What do you think Copilot needs from you before it can answer well?

**Watch for:** Point out that there is no file to attach. If a learner's Teams looks different from the lab, that's normal.

#### Try Out 9: Catch up in 2 minutes _(7 min)_

**Say:** Try Out 9: catch up in two minutes. Open the channel, click Copilot, paste prompt 1 and press Send. Then paste the follow-up that asks who said what about the logistics invoice and the duplicate payments.

**Ask:** Before you press Send, what do you expect the summary to say is still open?

**Watch for:** Start a timer. The prompt must be pasted exactly as written, so look for people retyping it. Point at the copy button on each prompt box. The result in the lab is an illustrative example.

#### Try Out 9: Check the summary _(4 min)_

**Say:** Now check the summary, because that's the real skill. Follow each citation back to its message, because the number links the point to its source. Flag any owner or date the chat doesn't give, since the summary is only as good as the messages it cites.

**Ask:** Which point in the summary could you not trace to a message?

**Watch for:** Follow each citation back to its message in the chat. Then check who said what: 'may explain it' is a claim, not evidence.

#### Try Out 10: Prepare tomorrow’s status meeting _(8 min)_

**Say:** Try Out 10: prepare tomorrow's status meeting. Stay in the channel, click Copilot, paste prompt 2 and press Send. It asks for a 30-minute agenda, five questions and the evidence we still need. Then paste the follow-up that drafts a short message to the team, and do not post it.

**Ask:** What would a useless agenda look like, and how would you spot it?

**Watch for:** The agenda must come from the real open items, not generic audit topics. Watch for anyone about to post the draft message. Leave it unposted.

#### Try Out 10: Check the agenda and the message _(4 min)_

**Say:** Check the agenda against the channel. Every agenda item, every question and every evidence line should link to a message, and questions should name an amount or an ID. Then read the draft message and leave it unposted, because you decide when to send, in your own Teams.

**Ask:** Which evidence line has no ER number yet, and who should own it?

**Watch for:** Point at the bottom line: the declaration, approval, duplicate check, slow-moving review and tax support have no ER number. Generic topics are the warning sign.

#### Refine: Action summary _(6 min)_

**Say:** Refine: the action summary. This step is mandatory. Click Copilot in the channel, paste the Refine prompt, and ask for every action with an owner and a due date, flagging anything with no owner or no date. Then paste the follow-up to post it, in the training chat only.

**Ask:** Why do you think a missing owner matters more than a missing detail?

**Watch for:** Start a timer. The word 'flag' is the point: Copilot must not invent an owner or a date. The post is training chat only.

#### Refine: Check the action list _(3 min)_

**Say:** Check every owner and date against the chat. Where the chat gives none, the row should say no owner or no date, so flag it and don't fill it in. Then post the list in the training chat only.

**Ask:** Which action has no owner at all, and who should be asked to take it?

**Watch for:** Point at the counts and the last row, where F-05's 28 February target is after the 20 February board meeting. A tidy list can hide an owner nobody named.

#### Review: The six questions _(2 min)_

**Say:** Last check: the six questions. Source, evidence, status, audience, action and professional boundary. Ask them of every result you plan to use. Finishing the checks doesn't approve the result, because a person decides.

**Ask:** Which of the six questions would catch the mistake you are most likely to make?

**Watch for:** 'Professional boundary' is the one people don't know: no audit opinion, and no claim that management agreed. This step is mandatory.

#### What you learned today _(2 min)_

**Say:** Today you did three things with Copilot in Teams. You caught up on a busy channel with citations, planned a status meeting from the real open items, and built an action list that flags every gap. Keep three habits: check against the messages, keep the gaps visible, and let a person decide.

**Ask:** Which busy chat or channel could you catch up on this week, and check against the original messages?

**Watch for:** End on the habit, not the tool. The summary is only as good as the messages it cites.

## Session 6: Copilot Chat

[Open the lab](./lab/06-copilot-chat.md) · The engagement leader needs a briefing today and wants six suspicious matters investigated across the client file, the transaction data and the supporting documents.

**Words to teach:** Evidence trail (The same amount followed from file to file, to see what supports it.); Exposure (The money that could be wrong or at risk. A possible amount, not a proven loss.); Confirmed or assumed (Confirmed means a document says it. Assumed means someone, or Copilot, supplied it without proof.); Year-end revenue (A sale booked right at the year end. The team checks it truly belongs in that year.); Related party (A company linked to the client or its leaders. Deals with them need extra care.); Dormant vendor (A supplier marked inactive in the records. Paying one is unusual and needs a reason.)

#### Your role and your job today _(1 min)_

**Say:** You've just joined the engagement team, and the engagement leader needs a briefing today. Six matters look suspicious, and the evidence is spread across three files. You'll produce three things: a one-page briefing, a group investigation, and a set of numbers you've verified.

**Ask:** Which of the three jobs would you find hardest?

**Watch for:** Point at the three jobs and say these are the only three things we'll do. Meridian’s timeline is background, so don't read it out.

#### Which file do you trust? _(1 min)_

**Say:** Three files go into one chat: the client background, the transaction data and the supporting documents. Each file has a warning, so read it before you trust the file. When two files disagree, we say so. We never pick one quietly.

**Ask:** If two files give different dates for the same item, what do you do next?

**Watch for:** Point at the example under the table: journal JRN-000002 in `04_Audit_Analytics.xlsx` is posted on 27 December, but invoice MEL-261231 in `06_Supporting_Documents.pdf` is dated 31 December. Also read the `04_Audit_Analytics.xlsx` warning aloud: it holds a trainer sheet, and learners must not open it or ask Copilot about it.

#### Download the three files _(1 min)_

**Say:** Now we get the three files. Download one from the list, or take all three in the ZIP. It's all made-up training data, so it's safe to download.

**Ask:** Can everyone download files on this computer?

**Watch for:** A locked-down laptop may block downloads. Find that out now, not at minute 20. Even better, ask people to do this step before the session.

#### Save all three in OneDrive _(3 min)_

**Say:** For this lab, the three files need to live in OneDrive or SharePoint. Open OneDrive in your browser, make a folder called Meridian Chat, and upload all three files. Your company's setup may look different, so check in your own environment.

**Ask:** Can everyone open OneDrive right now?

**Watch for:** The usual stall is files still sitting in Downloads. Walk the room and look for the folder on each screen.

#### The prompt formula and three habits _(2 min)_

**Say:** A prompt is just what you type to Copilot. A good one is a single sentence with seven parts: role, task, source, focus, format, limit and a check. Spot each part in the Meridian example, then keep the three habits in view.

**Ask:** Which of the seven parts do you think people forget most?

**Watch for:** Tap each part of the example as you name it. The source and the check are the two parts people skip, and they matter most. Read the ground rule aloud: no personal or client data in prompts.

#### Explore the three files _(3 min)_

**Say:** Before you ask across three files, know what's in each one. Open each file and note one amount that could show up in more than one file. That amount is where today's evidence trail starts.

**Ask:** Which amount do you think will turn up in more than one file?

**Watch for:** Start a 3-minute timer. The key under the table says which rows are plain facts and which are a gap or warning. Read the `04_Audit_Analytics.xlsx` warning aloud: it is a training extract, so nobody should try to match it to the financial statements.

#### Open Copilot Chat and add your files _(4 min)_

**Say:** This is the demo, so just watch the flow. You open Copilot Chat on the web, add all three files with + Add files or a forward slash, and then you're ready to ask. Buttons can differ, so check in your own environment before you copy me.

**Ask:** Why add all three files before asking, instead of one at a time?

**Watch for:** Pause at the file picker and read the three file names aloud, because they look alike. Remind them the files must be in OneDrive or SharePoint. If a learner's screen looks different from the lab, that's normal.

#### Try Out 11: Brief the engagement leader _(6 min)_

**Say:** Try Out 11: brief the engagement leader. Add all three files, paste prompt 1 and press Send, then paste the follow-up. The follow-up asks which points a document confirms and which are Copilot's assumptions. Use the copy button on each prompt box, so nobody mistypes.

**Ask:** Before you press Send, which risk do you expect to see in the top five?

**Watch for:** Start a 6-minute timer. Look for people retyping the prompt, or asking before all three files are added. Point at the copy button on each prompt box.

#### Try Out 11: Check the briefing _(4 min)_

**Say:** Now check the briefing, because that's the real skill. Every point should name a file, and every amount should match the file exactly. Then sort the points: what a document confirms, and what Copilot assumed.

**Ask:** Which point did Copilot work out itself, instead of reading it from a file?

**Watch for:** The order of the top five risks is Copilot's own ranking, so it carries the Assumed label. Point at that row. Also point at the Inferred rows. For example, the SGD 1,250,000 journal and the bank credit look like one event, but no document says so. The example result is an illustrative example, so check your own answer.

#### Choose your group topic _(4 min)_

**Say:** Now we work in groups: each group takes one of the six topics, assigned by you or chosen by them. Pick a topic and see one amount appear in more than one file, which is the evidence trail. Try the inventory topic: SGD 2.3m in transit appears only in the interview notes. Those notes aren't uploaded here, so it's an assumption.

**Ask:** In your topic, which file shows the amount first, and where else does it turn up?

**Watch for:** Open topic 5, Inventory, and point at the Assumed row, the one with no source here. A number in only one place, with no document behind it, is an assumption. Then remind them to replace [our group topic] with their topic name. The trail is an illustrative example, so check Copilot's own answer.

#### Try Out 12: Group investigation _(7 min)_

**Say:** Try Out 12: investigate your group topic. Stay in the same conversation and put your topic into the gap in prompt 2. Then send it. Then paste the follow-up, which asks for three sentences you could say in one minute.

**Ask:** What do you want the engagement leader to remember after one minute?

**Watch for:** Start a 7-minute timer. The prompt has a gap, [our group topic], so look for anyone pasting it unchanged. A new chat needs all three files added again.

#### Try Out 12: Check the evidence trail _(4 min)_

**Say:** Check the evidence trail. Find the same amount in more than one file, and note the file and place for each point. Then mark each point as confirmed, inferred, assumed, conflicting or unresolved.

**Ask:** Where does your trail rest on an assumption instead of a document?

**Watch for:** The evidence trail follows the topic you chose. Point at the exposure line: it's a possible amount, not a proven one. Read the three-sentence pitch aloud. It should take about a minute.

#### Refine: Verify every number _(6 min)_

**Say:** Refine: make Copilot show its sources. In the same conversation, paste the Refine prompt. It asks for the exact file and place of every number Copilot quoted, and to remove what it can't support. Then paste the follow-up and compare with another group.

**Ask:** Which number in your investigation are you least sure of?

**Watch for:** Start a 6-minute timer. This step is mandatory. Copilot checking itself is only a start, and your own check is the next step.

#### Refine: Check the numbers _(3 min)_

**Say:** Now you check the numbers. Each one needs an exact file and place. Decide for each number whether to keep it or remove it. Remove anything you can't support, even if it sounds right.

**Ask:** Which number would you remove first, and why?

**Watch for:** Each topic has one planted claim marked Assumed, and the page removes it for you after a moment. For Inventory it's the SGD 2.3m in transit. Point at it: a number with no file and no place is an assumption. Ask groups to swap and compare conclusions.

#### Review: The six questions _(2 min)_

**Say:** Last check: the six questions. Source, evidence, status, audience, action and professional boundary. Ask them of every result you plan to use. Finishing the checks doesn't approve the result, because a person decides.

**Ask:** Which of the six questions would catch the mistake you are most likely to make?

**Watch for:** 'Professional boundary' is the one people haven't met. It means no audit opinion and no accusation, and exposure is possible, not proven. Point at that row. This step is mandatory.

#### What you learned today _(2 min)_

**Say:** Today you did three things with Copilot Chat. You briefed a leader from three files, followed one amount across them, and verified every number. Keep three habits: name the file, keep the gaps visible, and let a person decide.

**Ask:** Which briefing at work could you rebuild from its source files this week, naming a file for every number?

**Watch for:** Leave the closing question up and let people answer. Point at the link to the next session. Say it once more: Copilot proposes, the team verifies.

> [!IMPORTANT]
> Copilot proposes; the team verifies. This is a training exercise, not audit or tax advice.
