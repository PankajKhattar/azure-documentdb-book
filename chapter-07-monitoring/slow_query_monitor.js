const { MongoClient } = require("mongodb");

async function run() {
  const client = new MongoClient("mongodb://localhost:27017");
  await client.connect();

  const db = client.db("shop");

  const start = Date.now();

  await db.collection("orders")
    .find({ status: "completed" })
    .toArray();

  const latency = Date.now() - start;

  console.log("Query latency:", latency, "ms");

  if (latency > 100) {
    console.log("WARNING: Slow query detected");
  }
}

run();