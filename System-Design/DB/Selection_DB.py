https://towardsdatascience.com/choosing-the-right-database-in-a-system-design-interview-b8af9c6dc525

Selection:
	Cost, Scalability, Performance
	Understand and document information requirements. What information about what subject must be retained for future use by the system?

When choosing a database, it is important to consider data size, structure, relationships, and how important it is to enforce schemas and ensure consistency.
it's ok to choose more than one.

Suppose you want to build a reporting system for how many people bought a particular item. Now, on amazon products are sold by a variety of users, of different brands and different variations. 
So the report can not target a single product, rather it should target a subset of products, which can be in either Cassandra or MySQL. Such a requirement is an example of a situation where our best choice would be a document DB like Mongo DB. 
So we decide to keep a subset of this orders data in Mongo DB that tells us which users bought how much quantity of a certain product, at what time, on what date, etc. 
So suppose you want to check how many people bought sugar in the last month, you can get order ids from Mongo DB, and use this order id to pick up the rest of the data from Cassandra or MySQL.

Factors
	Structure of the data
	Query pattern
	Amount or scale that you need to handle
Example: Amazon - Cart - need ACID, so need RDBMS but lots of attributes - need Cassandra

Type of DB:
1. RDMS:
	Homogeneous
	Scalability
	Fexibility
	ACID (Atomicity, Consistency, Isolation, Durability)
	Tables - Schema doesnot change
	Not aware of relation
	Microsoft SQL, Oracle, MySQL, and Postgres
2. NoSql:
	Heterogeneous
	Schema Agnostic
	MongoDB, Riak, Amazon S3, Cassandra, and Hbase.
	One drawback of NoSQL databases is that they have ”eventual consistency,” meaning that all nodes will eventually have the same data.
3. Column Based:
	Accelerates analyses because the system only has to read the locations your query is interested in, all within a single column.
	These systems compress repeating volumes in storage, allowing better compression, since the data in one specific column is homogeneous across all the columns 
	Slower, Inserts and updates on an entire row (necessary for apps like ERPs and CRMs, for example) can be expensive.
4. Cloud solutions:
	ISsue - B/W Limitation, Cost, Compliance and Security
5. Caching Solutions - Redis, Memcached
6. File Storage solutions - S3 + CDN
7. Storage Solutions Offering Text Search Capability _ Elasticsearch
8. Time Series Database - InfluxDB, OpenTSDB


