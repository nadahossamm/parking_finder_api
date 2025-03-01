from flask import request, jsonify
import user_operations.validator as validator
import datetime as dt


def create(collection_ref, db):
    try:

        doc_ref = db.collection(collection_ref)
        if len(doc_ref.get()) != 0:
            doc_ref = db.collection(collection_ref).document()
            request.json.update({'id': doc_ref.id})

            if collection_ref == "Review":
                request.json.update({'date': dt.datetime.now()})

            validated, errors = validator.validate(
                request.json, collection_ref, is_required=True)

            if validated:
                doc_ref.set(request.json)
                return jsonify(f"Document is added successfully"), 200

            else:
                return errors
        else:
            return "collection doesn't exist"
    
    except Exception as e:
        return f"An Error Occurred: {e}"


def get(collection_ref, db):
    try:
        
        doc_ref = db.collection(collection_ref)
        if len(doc_ref.get()) != 0:    
            if request.json:
                doc_id = request.json['id']

                if doc_id:
                    if doc_ref.document(doc_id).get().exists:
                        doc = doc_ref.document(doc_id).get()
                        return jsonify(doc.to_dict()), 200

                    else:
                        return "document doesn't exist"
            else:
                all_docs = [doc.to_dict() for doc in doc_ref.stream()]
                return jsonify(all_docs), 200
        
        else:
            return "collection doesn't exist"
    
    except Exception as e:
        return f"An Error Occurred: {e}"


def update(collection_ref, db):
    try:

        doc_ref = db.collection(collection_ref)
        if len(doc_ref.get()) != 0:
            validated, errors = validator.validate(
                request.json, collection_ref, is_required=False)

            if validated:
                doc_id = request.json['id']

                if doc_ref.document(doc_id).get().exists:
                    doc_ref.document(doc_id).update(request.json)
                    return jsonify("Document is updated successfully"), 200

                else:
                    return "document doesn't exist"
            
            else:
                return errors
        else:
            return "collection doesn't exist"
    
    except Exception as e:
        return f"An Error Occurred: {e}"


def delete(collection_ref, db):
    try:

        doc_ref = db.collection(collection_ref)
        if len(doc_ref.get()) != 0:
            doc_id = request.json['id']

            if doc_ref.document(doc_id).get().exists:
                doc_ref.document(doc_id).delete()
                return jsonify("Document is deleted successfully"), 200

            else:
                return "document doesn't exist"
        
        else:
            return "collection doesn't exist"
    
    except Exception as e:
        return f"An Error Occurred: {e}"
