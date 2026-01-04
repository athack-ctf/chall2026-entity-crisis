# @HACK 2026: Entity Crisis

> A deliberately vulnerable web challenge that explores XML parsing vulnerabilities and the risks of enabling certain parser features.

## Challenge Type

- [ ] **OFF**line
- [X] **ON**line

## Design Type

- [X] **Black**-Box
- [ ] **White**-Box

## Designer(s)

- Tarek Hamze

## Description

This challenge is built around a real world vulnerability: applications that accept **XML input** and process it with a parser configured to support advanced features (e.g., DTD handling and entity expansion). When an application treats XML as “just data” and doesn’t carefully constrain what the parser is allowed to resolve, user input may trigger **local resource access** such as performing an XXE injection attack that retrieves an arbitrary file from the server's filesystem.

Participants interact with a simple space shop web app that performs “availability/stock checks” by sending XML to a backend endpoint. The challenge tests whether participants can leverage the XML processing surface accordingly. In other words, perform an XXE injection attack to retrieve etc/passwd that contains the flag. Some guessing is involved, players have to guess that etc/passwd is the file they should access.

### Educational goals

The challenge is designed to test the following skills:

- Understanding of **XML structure** (elements, attributes)
- Awareness of **parser configuration** and why defaults/features matter
- Practical traffic inspection and manipulation using **Burp Suite / Repeater** (or curl)

**IMPORTANT:** This description will **NOT** be shared with participants.

## Category(ies)

- `web`

---

# Project Structure

## 1. HACKME.md

- **[HACKME.md](HACKME.md)**: A description of the challenge to be shared in CTFd.

## 2. Source Code

- **[source/README.md](source/README.md)**: Instructions for running the challenge locally from source.
- **[source/*](source/)**: Your source code.

## 3. Offline Artifacts [OPTIONAL]

## 4. Solution

- **[solution/README.md](solution/README.md)**: A detailed writeup of the working solution.
- **[solution/FLAGS.md](solution/FLAGS.md)**: A single markdown file listing all (up-to-date) flags.
- **[solution/*](solution/)**: Any additional files or code necessary for constructing a reproducible solution for the challenge.

## 5. Dockerization

> **NOTE:** Online challenges must be containerized for deployment. During early development, focus on correctness first; container hardening can be refined later.

- **[source/main/Dockerfile](source/main/Dockerfile)**: Needed for building a containerized image of the web page.
- **[source/docker-compose.yml](source/docker-compose.yml)**: Needed for a configuration-free run of the online challenge.
