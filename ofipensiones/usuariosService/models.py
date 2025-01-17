from mongoengine import Document, fields, EmbeddedDocument


class Usuario(Document):
    nombreUsuario = fields.StringField(max_length=100, required=True)
    tipoUsuario = fields.StringField(max_length=50, required=True)
    institucionId = fields.ObjectIdField(editable=False)
    nombreInstitucion = fields.StringField(max_length=100, required=True)

    def __str__(self):
        return self.nombreUsuario

# class PadreFamilia(Usuario):
#     hijos = fields.ListField(fields.StringField(max_length=100))
#
#     def __str__(self):
#         return self.nombreUsuario