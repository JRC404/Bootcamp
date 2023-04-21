namespace Lloyds
{
    public class User {
        public string myUserName;
        public string myLocation;
        public User(string Username, string Location) {
            myUserName = Username;
            myLocation = Location;
        }

        public void DisplayInformation() {
            Console.WriteLine("My name is: " + myUserName);
            Console.WriteLine("My location is: " + myLocation);
        }
    }
}

