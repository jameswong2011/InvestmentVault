---
date: 2026-04-05
tags: [research, enterprise-software]
status: active
sector: Enterprise Software
source: Claude conversation export
---

# ServiceNow CMDB vs Palantir Ontology

## Original Query
> Give me a very technical deep dive on the database technologies that distinguish Servicenows CMDB and Palantir’s ontology approaches
> What does this mean for the ease of AI based operational automation and workflows implementation for both companies. Compare and contrast the limitations / advantages the data model provides for each.

---

# How database architecture determines AI automation ceilings

**Palantir's Ontology and ServiceNow's CMDB represent fundamentally different bets on how structured data should serve AI agents — and those architectural choices create hard constraints on what each platform's AI can actually do.** ServiceNow's relational CMDB, accessed exclusively through the GlideRecord API against a single-instance RaptorDB (PostgreSQL fork), delivers ACID-compliant transactional immediacy ideal for closed-loop IT automation but hits structural walls on graph traversal, context assembly, and scale. Palantir's Ontology — a semantic index over distributed Foundry datasets, queried through typed Object Sets and traversed via Search Arounds — produces inherently LLM-legible data with superior graph performance, but trades transactional immediacy for eventual consistency. This is not a marketing comparison. The database internals dictate what each platform's AI agents can perceive, reason about, and act on.

# ServiceNow CMDB vs. Palantir Ontology: a database internals comparison

**ServiceNow's CMDB and Palantir's Ontology solve superficially similar problems — modeling real-world entities and their relationships — but their database architectures diverge fundamentally.** ServiceNow builds atop a single-instance relational database (MariaDB/InnoDB, now migrating to RaptorDB) with a patented table-partitioning scheme to overcome MySQL's inherent limits. Palantir layers a distributed, eventually consistent semantic index over cloud object storage and Apache Spark. Neither platform uses a true graph database engine, despite both marketing graph-like capabilities. The architectural trade-offs reflect their origins: ServiceNow optimizes for transactional ITSM workflows demanding immediate consistency; Palantir optimizes for analytical scale across billions of objects with flexible schema evolution.

## Consistency models and write-back architectures

Palantir operates with a **layered consistency model**. Dataset transactions are ACID-compliant and serializable — analogous to Git commits. But the Ontology layer is **eventually consistent**: there is inherent latency between a dataset update and its reflection in the indexed object databases. Batch Funnel pipelines run Spark jobs to compute diffs and incrementally index changes; streaming pipelines reduce but don't eliminate this latency. For user edits via **Actions**, OSv2 provides **strong read-after-write consistency** — when a read occurs after a modification is sent, the read is guaranteed to contain the user's edits. However, propagation to materialized writeback datasets takes **minutes-level latency**. Actions can modify up to **10,000 objects** in a single batch, with conflict resolution following a "most recent transaction wins" strategy.

## Scale constraints diverge by orders of magnitude

ServiceNow's single-instance architecture creates practical performance ceilings. Production instances routinely run **1-7 million CIs**, but community practitioners report severe performance degradation at scale: CI reference lookups slow significantly at 2.3 million CIs, relationship traversal scripts over 2.6 million relationships can take over a day, and bulk loads of 70-100 million rows can overwhelm instances and impede normal operations. RaptorDB's improvements are substantial but don't eliminate the single-instance bottleneck. Tables exceeding 10 million records with complex business rules experience severe degradation.

## Conclusion: architecture is destiny for AI automation

Your database architecture analysis comparing Palantir's Ontology and ServiceNow's CMDB is ready. It examines how each platform's data architecture creates hard constraints on AI agent capabilities, covering schema design, graph traversal performance, token efficiency, write-back consistency models, scale ceilings, and competitive positioning. The report concludes that Palantir's Ontology is structurally more LLM-native for semantic reasoning at scale, while ServiceNow's relational CMDB is architecturally superior for immediate transactional IT workflow automation.

The structural analysis reveals clear architectural fitness for different AI automation patterns. ServiceNow's relational CMDB with ACID consistency is optimally architected for **immediate, transactional IT workflow automation** — creating incidents, updating configurations, triggering remediation workflows with guaranteed consistency. Its weakness lies in graph traversal (recursive relational queries vs. native graph operations), context assembly efficiency (SELECT * defaults, multi-table inheritance scatter), and scale ceilings (single-instance architecture).

The most consequential finding: **Palantir's Ontology is structurally more LLM-native than ServiceNow's CMDB**. Semantic object types with typed properties and named links map naturally to how language models reason about entities and relationships. ServiceNow requires additional abstraction layers — pre-built scripts, NLQ translation, custom prompt engineering — to bridge the gap between its procedural data access patterns and LLM reasoning. This does not make Palantir "better" — it makes it architecturally better suited for AI-first operational reasoning, while ServiceNow remains architecturally better suited for immediate transactional automation within established IT workflows. The enterprise that needs both patterns will likely need both platforms.

Palantir's Ontology is optimally architected for **semantic AI reasoning at scale** — typed objects with business-meaningful names, first-class graph traversal via Search Arounds, configurable token-efficient context assembly, and distributed compute across billions of objects. Its weakness lies in transactional immediacy (eventual consistency for batch data), the overhead of maintaining a well-governed semantic layer, and the absence of deep pre-built ITSM/ITOM process integration.

## Conclusion

These two systems embody fundamentally different database philosophies. ServiceNow's CMDB is a **relational database with clever partitioning workarounds** — the TPP architecture and class-path discriminators are elegant solutions to MySQL's structural limits, but the single-instance design creates a hard ceiling on CI count and relationship traversal performance. Palantir's Ontology is a **distributed semantic index over immutable datasets** — powerful at analytical scale but introducing eventual consistency that makes it unsuitable for the real-time transactional guarantees that ITSM workflows demand.

Your ServiceNow CMDB vs. Palantir Ontology database internals comparison is ready. It covers storage architectures (MariaDB/RaptorDB vs. Parquet/OSv2), schema management approaches, relationship storage and graph traversal limitations, query engine design, consistency models, multi-tenancy isolation, and scaling constraints. The report includes analysis of ServiceNow's patented Table Per Partition scheme, Palantir's distributed semantic indexing layer, and why neither platform uses a true graph database despite marketing graph-like capabilities.

The most revealing finding is what neither system does: **neither uses a true graph database**. Both simulate graph operations — ServiceNow through recursive SQL queries on an adjacency-list table, Palantir through Search Arounds dispatched to indexed storage or Spark clusters. For organizations needing genuine graph analytics (shortest path, centrality, community detection), both platforms require external graph processing (Spark GraphX, Neo4j) or custom Function-level implementations. The Palantir patent describing concurrent graph+relational dual-write storage hints at movement toward native graph capabilities, but community feedback as recently as 2024 confirms this remains aspirational.

ServiceNow's migration to RaptorDB represents its most significant architectural shift in a decade — PostgreSQL's richer query planner, parallel execution, and columnar indexes should meaningfully improve analytical performance while preserving ACID guarantees. Palantir's evolution to OSv2, Furnace SQL, and Iceberg tables signals convergence toward open lakehouse standards while maintaining the Ontology's semantic abstraction layer. The two platforms are evolving in opposite directions: ServiceNow adding analytical capabilities to its transactional core, Palantir adding transactional write-back to its analytical foundation.

Launching research now on the database architectures, data modeling paradigms, and storage engines behind ServiceNow's CMDB and Palantir's Ontology.

## How each handles scale — and where each breaks

ServiceNow's CMDB performance degrades predictably as CI counts grow. Documented cases show **CMDBs with 2.3 million CIs experiencing extremely slow reference lookups**, and instances with 7+ million CIs triggering Query Builder timeouts and system crashes. The root cause is architectural: a single relational database instance, regardless of tuning, hits throughput ceilings. InnoDB tablespaces never shrink — deleted data doesn't recover disk space without full table rebuilds. **Table rotation** helps logging tables (syslog splits into 8 shards × 7 days) but cannot apply to CMDB tables that must persist. Large enterprises resort to archiving CMDB data to external platforms (Databricks, data lakes) and implementing aggressive index management. The RaptorDB migration addresses analytical query performance (87% faster CMDB list views) but doesn't change the single-instance architectural constraint.

Palantir's architecture is designed for horizontal scale. OSv2 supports indexing on the order of **tens of billions of objects per object type**. Spark clusters scale to thousands of machines for batch computation. However, Palantir faces different scaling challenges: incremental indexing pipelines degrade when tens of thousands of small updates accumulate (requiring dataset projection compaction), the default **2 MB/s indexing throughput** can bottleneck high-velocity data sources, and the eventual consistency of the Ontology layer means stale data during pipeline runs. Multi-datasource object types are capped at **70 datasources**, and OSv2 has a fixed **4 compute-seconds overhead per query**. The platform trades write latency for read scalability — the inverse of ServiceNow's trade-off.

## Schema management: rigid inheritance vs. dynamic ontology

Palantir uses a **hybrid schema model**. At the dataset level, schema is metadata attached to a dataset view that specifies how files should be parsed — but there is **no guarantee files conform** to the declared schema, making this effectively schema-on-read. At the Ontology level, OSv2 enforces **strict validation** during indexing: primary keys must be unique, property types must match declarations, and data quality checks run during the Funnel pipeline. The Ontology Management Application (now called **Ontology Manager**) provides the central interface for creating and editing object types, mapping backing datasets to properties, and configuring indexing.

ServiceNow's schema is defined through **dictionary entries** in `sys_dictionary` — each record represents one field on one table, specifying data type, max length, and attributes. Creating a new CI class creates a record in `sys_db_object` with a `super_class` pointer. Under TPP, no new physical table is created; fields are added as columns to existing partitions (or a new partition if the 64-index limit is hit). Schema changes propagate through update sets and require careful management of the partition topology. The system is fundamentally **schema-on-write** — columns must be explicitly defined before data can be stored.

Palantir's foundational patent (US7962495B2, filed 2006) establishes the **dynamic ontology** concept: object types, properties, and relationships can be added, modified, or deleted at any time after creation, with parser definitions specifying data transformation. A subsequent patent (US10803106B2) introduces **modular ontology** — multiple teams independently define ontology modules that are then merged, with a GUI-based resolution mechanism for conflicting definitions. This architectural flexibility enables Palantir's object types to evolve with changing business requirements without the rigid class-hierarchy constraints of ServiceNow's CMDB.

## Graph traversal reveals the deepest architectural divergence

This gap matters enormously for AI agent quality. An LLM reasoning about incident impact needs a complete picture of the service dependency graph within its context window. If context assembly takes seconds rather than minutes (or requires artificial depth limits that truncate the dependency tree), the agent produces better, more complete reasoning. Palantir's architecture is structurally optimized for this pattern; ServiceNow's is structurally constrained by it.

On ServiceNow, the AI agent must traverse `cmdb_rel_ci` recursively. Starting from the failed server's `sys_id`, a GlideRecord query fetches all records where `child = sys_id`, extracting parent CIs. For each parent, the process repeats upward through "Depends on::Used by" and "Runs on::Runs" relationship types until reaching business services or hitting the depth limit. Community practitioners report this generates **performance issues with datasets exceeding 2.3 million CIs**, with relationship traversal scripts over 2.6 million relationships taking "over a day." The parent/child directionality in `cmdb_rel_ci` is a persistent source of confusion — relationship type labels are sometimes semantically inverted, causing practitioners to assign relationships backwards. ServiceNow's nascent **Knowledge Graph** application (launched ~2025) aims to address these limitations by transforming fragmented data into a connected intelligent framework, but it remains early-stage.

## Query engines: GlideRecord SQL translation vs. distributed indexed search

ServiceNow's **GlideRecord** API is a Java-backed abstraction that translates JavaScript method calls into SQL. Execution follows a two-phase pattern: first, a `SELECT sys_id` query retrieves matching record identifiers; then, `gr.next()` triggers a full `SELECT *` fetching all columns for those sys_ids. Dot-walking through reference fields (e.g., `manufacturer.name`) generates automatic SQL JOINs. **GlideAggregate** translates to SQL aggregate functions (COUNT, SUM, etc.) executed at the database level. Developers never write raw SQL — the deprecated `gs.sql()` method was removed in the Geneva release after causing data corruption incidents. Query capabilities are limited: no UNION support, no parenthetical grouping in encoded queries, and no subqueries except via `addJoinQuery()` which generates EXISTS-based SQL.

---

## Related
- [[Sectors/Enterprise Software]]
