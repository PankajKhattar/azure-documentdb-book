const { MongoClient } = require("mongodb");

async function run() {

  const uri = "mongodb://localhost:27017";

  const client = new MongoClient(uri);

  try {

    await client.connect();

    console.log("Connected to Azure DocumentDB");

    const db = client.db("shop");
    const collection = db.collection("orders");

    const pipeline = [
      {
        $match: {
          operationType: "insert"
        }
      }
    ];

    const changeStream = collection.watch(pipeline);

    console.log("Listening only for INSERT events");

    changeStream.on("change", (change) => {

      console.log("Insert event detected");
      console.log(JSON.stringify(change.fullDocument, null, 2));
    });

  } catch (err) {

    console.error("Error:", err);
  }
}

run();