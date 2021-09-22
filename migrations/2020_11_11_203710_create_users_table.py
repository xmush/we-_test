from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name', 50)
            table.string('email').unique()
            table.text('password')
            table.string('role', 10)
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
