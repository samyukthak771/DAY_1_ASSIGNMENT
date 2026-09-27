# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The scenario chosen for this project is a Student Study Information Assistant.

The system works with private student information such as the student's name, department, semester, attendance, and internal marks. The same type of student request is handled using three different approaches: a plain chatbot, a rule-based workflow, and an AI agent.

The purpose is to understand how these three approaches differ in flexibility, decision-making, tool usage, private-data access, multi-step task handling, automation, and reliability.

---

## 2. Plain Chatbot

The plain chatbot uses an LLM to answer the user's question.

The user enters a study-related question, and the question is sent to the language model. The model generates a response based on the question.

The plain chatbot does not directly read the private student data file and does not use a separate tool or predefined decision-making workflow.

The main advantage of this approach is that it can answer many general questions flexibly. However, it cannot reliably answer questions that require the student's private information because the private data is not provided to the chatbot.

Therefore, the plain chatbot is mainly useful for general study questions and explanations.

---

## 3. Rule-Based Workflow

The rule-based workflow uses predefined conditions and the private student data stored in `private_data.json`.

The workflow first reads the private data file. It then checks the user's question against predefined rules.

For example, if the user asks about attendance, the workflow displays the attendance information. If the user asks about marks, it displays the internal marks. Other predefined conditions handle information such as the student's name, department, and semester.

The workflow does not use an LLM. Its decisions are based on fixed rules written by the programmer.

The main limitation is that it can only handle situations that have been anticipated and programmed into the rules.

---

## 4. AI Agent

The AI agent combines an LLM, a tool, and a loop.

In this project, the agent uses the LLM to understand and generate responses. A tool is used to read the private student data from `private_data.json`.

The agent receives the user's question, reads the private data, provides the relevant information to the LLM, and generates a response. The loop allows the agent to perform more than one step while handling the request.

For example, when the user asks for Python attendance and internal marks, the agent can access the private data and use the information to generate a natural-language answer.

The agent is more flexible than a fixed rule-based workflow because the LLM can interpret different forms of user questions. However, it also involves more components and can require more control and testing.

---

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for general questions | Limited to predefined rules | High |
| Decision-making | Mainly generates an LLM response | Uses fixed conditions | Uses LLM reasoning with tools and steps |
| Tool usage | No separate tool | Reads the data file directly | Uses a tool to access private data |
| Private-data access | No direct access | Yes | Yes |
| Multi-step task handling | Limited | Limited to programmed steps | Supports multiple steps using a loop |
| Automation | Basic response generation | Good for fixed tasks | Good for tasks requiring several actions |
| Reliability | Depends on the LLM response | Predictable for programmed cases | Depends on the LLM, tools, and implementation |

---

## 6. Suitability Analysis

For the selected student private-data scenario, the AI agent is suitable when the user needs flexible questions to be answered using private information and more than one step may be required.

The plain chatbot is useful for general study questions but does not directly access the private student data in this project.

The rule-based workflow is useful when the questions and required actions are predictable. It is simple and predictable, but new types of questions require additional rules to be programmed.

The AI agent combines an LLM with a tool and a loop. This allows it to understand the user's request, access the required private information, and perform multiple steps while generating the response.

Therefore, the three approaches are useful in different situations. The choice depends on whether the task needs general language generation, predictable predefined rules, or flexible multi-step interaction with tools and data.

---

## 7. Conclusion

A plain chatbot is appropriate for general questions, explanations, and conversations where external tools or private data are not required.

A rule-based workflow is appropriate for predictable tasks where the conditions and actions can be clearly defined in advance. It is simple and gives predictable results for the cases covered by its rules.

An AI agent is appropriate for tasks that require an LLM to understand a request, use tools, access information, and perform multiple steps.

This project demonstrates the difference between the three approaches. A plain chatbot mainly uses an LLM, a rule-based workflow follows predefined conditions without an LLM, and an AI agent combines an LLM, tools, and a loop to handle a task.