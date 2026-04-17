

- Improve /prune to archive old research notes that are not referenced by active theses or sector notes. This is to make sure /lint and /sync functions do not get burdened with reading too much text
- Should research commands /sync /sync all /compare /thesis etc. ignore metadata and vault integrity tasks and the user instead rely on /graph that is run after every incremental vault edit to capture metadata, linking and vault integrity changes. Long term /lint surfaces any document issues to be manually processed by Claude queries.