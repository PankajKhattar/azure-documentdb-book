import { MongoClient } from "mongodb";

const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

async function run() {
  await client.connect();

  const db = client.db("bookdb");
  const users = db.collection("users");

  await users.insertOne({
    userId: "u123",
    name: "Alice",
    preferences: {
      language: "en",
      notifications: true
    },
    createdAt: new Date()
  });

  console.log("Document inserted successfully");

  await client.close();
}

run().catch(console.error);
