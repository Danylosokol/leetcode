class Node {
    constructor(key, val){
        this.key = key
        this.val = val
        this.next = null
        this.prev = null
    }
}

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.cap = capacity
    this.cache = new Map()

    this.left = new Node(0, 0)
    this.right = new Node(0, 0)
    this.left.next = this.right 
    this.right.prev = this.left
};

/** Remove node from doubly linked list
 * @param {Node} node
 */
LRUCache.prototype.remove = function(node){
    const prev = node.prev
    const next = node.next

    prev.next = next
    next.prev = prev
}

LRUCache.prototype.insert = function(node){
    const prev = this.right.prev
    const next = this.right

    node.prev = prev
    node.next = next
    prev.next = node
    next.prev = node
}

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if(this.cache.has(key)){
        const node = this.cache.get(key)
        this.remove(node)
        this.insert(node)
        return node.val
    }
    return -1
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if(this.cache.has(key)){
        this.remove(this.cache.get(key))
    }

    const newNode = new Node(key, value)
    this.cache.set(key, newNode)
    this.insert(newNode)

    if(this.cache.size > this.cap){
        const lru = this.left.next
        this.remove(lru)
        this.cache.delete(lru.key)
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */