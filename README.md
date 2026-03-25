# Cat Search 🔍

A plugin for [Grinning Cat](https://github.com/matteocacciola/grinning-cat-core) that enables internet searches via
Google, returning a list of web pages with titles, descriptions, and links.

![thumb](thumb.png)

## Description

**Cat Search** integrates Google search capabilities directly into the Grinning Cat AI. When a user asks the Cat to
"search on Google", the plugin automatically triggers a search and returns the most relevant results formatted with
title, description, and URL.

## Features

- Performs Google searches on demand through natural language
- Returns structured results including:
  - **Title** of the web page
  - **Description** (snippet)
  - **URL** of the page
- Configurable number of results
- Configurable search language

## Installation

1. Copy the `cat-search` folder into the `plugins` directory of your Grinning Cat instance.
2. Install the required dependencies:

```bash
uv pip install -r requirements.txt
```

### Dependencies

- [`googlesearch-python`](https://pypi.org/project/googlesearch-python/)

## Usage

Simply ask the Cat to search on Google in your conversation:

> **"Search on Google: What is the capital of France?"**

> **"Search on Google: Who won the FIFA World Cup in 2018?"**

> **"Search on Google: What are the latest advancements in AI technology?"**

The Cat will respond with a list of results in this format:

```
**Title**: Example Page Title
**Description**: *A brief description of the page content...*
**URL**: https://example.com
---
```

## Settings

The plugin exposes the following configurable settings via the Grinning Cat admin panel:

| Setting             | Type  | Default | Description                                                  |
|---------------------|-------|---------|--------------------------------------------------------------|
| `number_of_results` | `int` | `10`    | Number of search results to return                           |
| `language`          | `str` | `en`    | Language code for the search results (e.g. `en`, `it`, `fr`) |

## Plugin Info

| Field          | Value                                                      |
|----------------|------------------------------------------------------------|
| **Version**    | 0.1.0                                                      |
| **Author**     | [Matteo Cacciola](https://github.com/matteocacciola)       |
| **Repository** | [cat-search](https://github.com/matteocacciola/cat-search) |
| **Tags**       | `google`, `search`                                         |

## License

See the repository for license information.