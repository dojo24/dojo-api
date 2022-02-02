const router = require('express').Router()
const db = require('../database/dbConfig')
const Squishies = require('./squishiesModel')

// all has /api/characters in front

router.get('/', (req, res, next) => {
    Squishies.findAll()
    .then(squishies => res.status(200).json({data: squishies}))
    .catch(err => next({ code: 500, message: 'Problems getting Squishies', err}))
})

router.get('/:id', (req, res) => {
    Squishies.findById(req.params.id)
        .then(squishy => {
            if (squishy) {
                res.status(200).json({data: squishy})
            } else {
                res.status(404).json({message: 'ID not found'})
            }
        })
        .catch(err => {
            res.status(500).json({message: 'Trouble getting Squishies', err})
        })
})

router.post('/', (req, res) => {
    Squishies.add(req.body)
        .then(squishy => {
            res.status(201).json({data: squishy})
        })
        .catch(err => {
            console.log(err)
            res.status(500).json({message: 'Trouble adding Squishies'})
        })
})

router.put('/:id', (req, res) => {
    Squishies.update(req.params.id, req.body)
        .then(squishy => {
            if(squishy) {
                res.status(200).json({data: squishy})
            } else {
                res.status(404).json({message: 'Id not found'})
            }
        })
        .catch(err => {
            console.log(err)
                res.status(500).json({message: 'Trouble updating Squishy'})
        })
})

router.delete('/:id', (req, res) => {
    Squishies.remove(req.params.id)
        .then(count => {
            if (count > 0) {
                res.status(200).json({message: "Squishy has been removed"})
            } else {
                res.status(400).json({message: 'ID not found'})
            }
        })
        .catch(err => {
            console.log(err)
            res.status(500).json({message: "Unable to remove that Squishy"})
        })
})

module.exports = router