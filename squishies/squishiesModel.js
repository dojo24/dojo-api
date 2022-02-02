const db = require('../database/dbConfig')

module.exports = {
    findAll,
    findBy,
    findById,
    add,
    update,
    remove
};

function findAll() {
    return db("squishies");
}

function findBy(filter) {
    return db("squishies")
    .where(filter).first();
}

function findById(id) {
    return db("squishies")
    .where({id}).first();
}

function add(squishy) {
    return db("squishies")
    .insert(squishy, "id")
    .then(ids => findById(ids[0]));
}

function update(id, changes) {
    return db("characters")
    .where({id})
    .update(changes, '*')
}

function remove(id) {
    return db("characters")
    .where({id}).del()
}