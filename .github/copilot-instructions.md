# Asia Learning Hub

This repository holds reusable learning and demo assets for the Asia MTT
community. `industry/` groups use cases by industry; the industry-level
READMEs currently serve as placeholders. Use `RULE.md` as the source of truth
for new use-case content and required product coverage.

## Industry use cases

- Add new cases under `industry/<Industry>/<Product>/<kebab-case-use-case>/`.
  Use the product directory names in `RULE.md`: `Copilot`, `Agent-Builder`,
  `Copilot-Studio`, `Foundry`, or `Fabric`. Put country-specific variants in
  a country/region subfolder when needed, rather than making the shared case
  country-specific.
- Each use-case `README.md` should cover the scenario, pain points, benefits,
  and demo steps. Agent Builder cases also document the agent configuration.
  For agents, Foundry, and Fabric, `RULE.md` requests environment/setup
  guidance in `setup.md`; its Agent-Builder diagram omits that file, so clarify
  the expectation before treating its absence as a violation.
- Keep supporting files with their use case: `data-files/` for Copilot,
  Agent Builder, and Copilot Studio; `source/` for Foundry code; `notebook/`
  and `data/` for Fabric assets. Use publicly available reference data and
  fictitious customer names.
- The existing FSI `Agent builder/Relationship Manager Assistant` case uses
  a legacy path and keeps its ZIP beside the README. Do not treat that path
  or its README's package link as the template for new cases; do not
  reorganize it unless the task calls for that change.

`RULE.md` also sets minimum case counts by product. Assess those as
repository-wide coverage, separately from whether an individual changed
case follows the layout and content rules.
