list = [ 4, 2, 8 ]


def getByIds():
    stack = []

    for i in range(len(list), 0, -1):
        rec = {
            "$cond": [
                { "$eq": [ "$_id", list[i-1] ] },
                i
            ]
        }
        if len(stack) == 0:
            rec["$cond"].push( i+1 )
        else:
            lval = stack.pop()
            rec["$cond"].push( lval )
    

        stack.append( rec )

# for (var i = list.length - 1; i > 0; i--) {

#     var rec = {
#         "$cond": [
#             { "$eq": [ "$_id", list[i-1] ] },
#             i
#         ]
#     };

#     if ( stack.length == 0 ) {
#         rec["$cond"].push( i+1 );
#     } else {
#         var lval = stack.pop();
#         rec["$cond"].push( lval );
#     }

#     stack.push( rec );

# }

    pipeline = [
        { "$match": { "_id": { "$in": list } }},
        { "$project": { "weight": stack[0] }},
        { "$sort": { "weight": 1 } }
    ]

    db.collection.aggregate( pipeline )