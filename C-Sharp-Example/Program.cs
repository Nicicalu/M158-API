using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.IO;
using System.Net;
using System.Text;
using RestSharp;
using Newtonsoft.Json;
using System.Windows.Forms;
using System.Data;

namespace C_Sharp_Example
{
    class Program
    {
        static void Main(string[] args)
        {
            string table = "Noten";
            var client = new RestClient("http://192.168.220.128:5000");
            // client.Authenticator = new HttpBasicAuthenticator(username, password);
            var request = new RestRequest("API/get");
            request.RequestFormat = DataFormat.Json;

            request.AddParameter("application/json", "{\"table\": \""+ table+"\"}", ParameterType.RequestBody);
            var response = client.Post(request);
            var content = response.Content; // Raw content as string
            Console.WriteLine(content);

            Application.EnableVisualStyles();
            Form frm = new Form();  // create aForm object
                frm.AutoSize = true;

            DataGridView dataGridView = new DataGridView();
                dataGridView.AutoSize = true;

            DataTable dataTable = (DataTable)JsonConvert.DeserializeObject(content, (typeof(DataTable)));
            dataGridView.DataSource = dataTable;

            frm.Controls.Add(dataGridView);
            frm.ShowDialog();
        }

    }
}
