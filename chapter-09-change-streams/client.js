const { MongoClient } = require("mongodb");

async function run() {
  const uri = "mongodb://localhost:27017";

  const client = new MongoClient(uri);

  try {
    await client.connect();

    console.log("Connected to Azure DocumentDB");

    const db = client.db("shop");
    const collection = db.collection("orders");

    console.log("Starting change stream listener...");

    const changeStream = collection.watch();

    changeStream.on("change", (change) => {
      console.log("=================================");
      console.log("Change detected");
      console.log(JSON.stringify(change, null, 2));
    });

  } catch (err) {
    console.error("Error:", err);
  }
}

run();