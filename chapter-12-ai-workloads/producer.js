const { MongoClient } = require("mongodb");

async function run() {

  const uri = "mongodb://localhost:27017";

  const client = new MongoClient(uri);

  try {

    await client.connect();

    console.log("Connected to Azure DocumentDB");

    const db = client.db("ai");

    const collection = db.collection("documents");

    const document = {
      title: "Distributed Systems",
      content: "Replication improves availability and resilience",
      category: "database",
      createdAt: new Date()
    };

    const result = await collection.insertOne(document);

    console.log("Document inserted");

    console.log(result);

  } catch (err) {

    console.error(err);

  } finally {

    await client.close();
  }
}

run();
